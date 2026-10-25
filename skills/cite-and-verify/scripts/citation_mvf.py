#!/usr/bin/env python3
"""
citation_mvf.py — Minimalist Validation Framework (MVF)

A lightweight, dependency-light reference verification layer that validates
BibTeX citations via arXiv, CrossRef/DOI, and NASA ADS APIs.

Usage:
    python citation_mvf.py --input citations.json --summary
    python citation_mvf.py --input my_citations.json    # custom input
    # ADS_API_TOKEN is read from the environment only.

Architecture:
    L1  — arXiv ID          → export.arxiv.org
    L2a — DOI               → api.crossref.org
    L2b — ADS bibcode       → api.adsabs.harvard.edu  (req. token)
    L3  — Title fallback    → api.openalex.org

All API results are SHA256-cached to ~/.cache/citation_mvf/ to avoid
re-validation. Adaptive rate-limiting respects provider quotas.

Outputs structured VerificationReport as JSON.
"""

import argparse
import hashlib
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


class _NoCredentialRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.URLError("credential-bearing redirects are refused")


def _credential_origin(url, hostname):
    parsed = urllib.parse.urlsplit(url)
    return (parsed.scheme == "https" and parsed.hostname == hostname
            and parsed.port in (None, 443) and parsed.username is None
            and parsed.password is None)


def _safe_urlopen(req, **kwargs):
    headers = {name.lower(): value for name, value in req.header_items()}
    destinations = {"authorization": "api.adsabs.harvard.edu", "x-api-key": "api.semanticscholar.org"}
    protected = [name for name in destinations if name in headers]
    for name in protected:
        if not _credential_origin(req.full_url, destinations[name]):
            raise urllib.error.URLError("credential destination is not allowlisted")
    if protected:
        return urllib.request.build_opener(_NoCredentialRedirect()).open(req, **kwargs)
    return urllib.request.urlopen(req, **kwargs)

# SSL context with certifi for systems missing root CAs
try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except (ImportError, FileNotFoundError):
    _SSL_CTX = ssl.create_default_context()

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CACHE_DIR = Path.home() / ".cache" / "transparent-science-citations-v1"
CACHE_SCHEMA = 3
CACHE_TTL_DAYS = 30  # re-verify after this many days
MAX_CACHE_FILES = 1000  # Cap cache size to prevent disk bloat

# Adaptive delays (seconds) between API calls — tuned for free-tier quotas
DELAYS = {
    "arxiv": 0.3,
    "crossref": 0.2,
    "ads": 0.4,
    "openalex": 0.2,
}

GLOBAL_TIMEOUT = 300  # total wall-clock budget for a verification run

_MVF_LOGS = []  # Internal error log for diagnostic purposes

# Regex patterns for ID extraction
RE_ARXIV = re.compile(r"(?:arxiv:|arXiv:|https?://arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5}(?:v\d+)?)", re.IGNORECASE)
RE_ARXIV_BARE = re.compile(r"^(\d{4}\.\d{4,5}(?:v\d+)?)$")
RE_DOI = re.compile(r"(?:doi:|DOI:|https?://doi\.org/)?(10\.\d{4,}/[^\s,;}]+)", re.IGNORECASE)
RE_ADS = re.compile(r"^(\d{4}[A-Z]{2,}[A-Z0-9\.]{5,})$", re.IGNORECASE)  # Strict ADS bibcode: Year + Journal + Volume/Page/Author


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------


def _cache_key(*parts: str) -> str:
    raw = "|".join((f"verifier-v{CACHE_SCHEMA}", *parts))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _cache_load(key: str) -> dict | None:
    path = CACHE_DIR / key[:2] / f"{key}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
        if data.get("_verifier_schema") != CACHE_SCHEMA:
            return None
        age = (datetime.now() - datetime.fromisoformat(data["_cached_at"])).days
        if age > CACHE_TTL_DAYS:
            path.unlink(missing_ok=True)
            return None
        return data
    except (json.JSONDecodeError, KeyError, OSError):
        return None


def _cache_save(key: str, data: dict) -> None:
    # Only cache successful results to avoid poisoning cache with transient errors
    if data.get("status") in ("verified", "low_confidence"):
        data = dict(data)
        data["_verifier_schema"] = CACHE_SCHEMA
        data["_cached_at"] = datetime.now().isoformat()
        path = CACHE_DIR / key[:2] / f"{key}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, default=str))

        # Enforce cache size limit (LRU eviction)
        all_files = list(CACHE_DIR.rglob("*.json"))
        if len(all_files) > MAX_CACHE_FILES:
            # Sort files by modification time (oldest first)
            all_files.sort(key=lambda p: p.stat().st_mtime)
            # Delete oldest until we are back under the limit
            num_to_delete = len(all_files) - MAX_CACHE_FILES
            for i in range(num_to_delete):
                all_files[i].unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _req(url: str, headers: dict | None = None, timeout: int = 15) -> dict | None:
    """Fetch JSON from URL; return an error marker on provider failures.
    Implements exponential backoff for 429 Rate Limit errors.
    """
    req = urllib.request.Request(url, headers=headers or {})
    max_retries = 3
    for attempt in range(max_retries + 1):
        try:
            with _safe_urlopen(req, timeout=timeout) as resp:
                if resp.status != 200:
                    return None
                body = resp.read().decode("utf-8")
                return json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_retries:
                # Exponential backoff: 2s, 4s, 8s...
                time.sleep(2 ** (attempt + 1))
                continue
            _MVF_LOGS.append(f"HTTP {e.code} for {url}: {e.reason}")
            return {"_request_error": True, "_http_status": e.code, "_detail": str(e.reason)}
        except (urllib.error.URLError, json.JSONDecodeError, OSError) as e:
            _MVF_LOGS.append(f"Request Error for {url}: {type(e).__name__} - {e}")
            return {"_request_error": True, "_detail": f"{type(e).__name__}: {e}"}
    return None


def _delay(domain: str, last_calls: dict[str, float]) -> None:
    """Sleep if needed to respect rate limits."""
    now = time.time()
    last = last_calls.get(domain, 0.0)
    gap = DELAYS.get(domain, 0.3)
    elapsed = now - last
    if elapsed < gap:
        time.sleep(gap - elapsed)
    last_calls[domain] = time.time()


def _title_similarity(expected: str, actual: str) -> float:
    """Return a simple normalized token overlap score for title checking."""
    expected_words = set(re.findall(r"[a-z0-9]+", expected.lower()))
    actual_words = set(re.findall(r"[a-z0-9]+", actual.lower()))
    return len(expected_words & actual_words) / max(len(expected_words | actual_words), 1)


# ---------------------------------------------------------------------------
# Verification backends
# ---------------------------------------------------------------------------

def verify_arxiv(arxiv_id: str, last_calls: dict[str, float], token: str | None = None) -> dict:
    """Verify an arXiv ID via the arXiv API (XML over HTTPS)."""
    import xml.etree.ElementTree as ET

    cache_key = _cache_key("arxiv", arxiv_id)
    cached = _cache_load(cache_key)
    if cached:
        return cached

    _delay("arxiv", last_calls)
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "citation_mvf/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
            body = resp.read().decode("utf-8")
        # Parse XML atom feed
        ns = {
            "atom": "http://www.w3.org/2005/Atom",
            "arxiv": "http://arxiv.org/schemas/atom",
        }
        root = ET.fromstring(body)
        total_results = root.find(".//opensearch:totalResults",
                                  {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"})
        n_results = int(total_results.text) if total_results is not None else 0
        if n_results > 0:
            entry = root.find("atom:entry", ns)
            title_el = entry.find("atom:title", ns) if entry is not None else None
            title = title_el.text.strip() if title_el is not None and title_el.text else None
            id_el = entry.find("atom:id", ns) if entry is not None else None
            returned = id_el.text.strip().split("/abs/")[-1] if id_el is not None and id_el.text else ""
            requested_base = re.sub(r"v\d+$", "", arxiv_id)
            returned_base = re.sub(r"v\d+$", "", returned)
            identity_ok = returned_base == requested_base and (not re.search(r"v\d+$", arxiv_id) or returned == arxiv_id)
            result = {
                "status": "verified" if title and identity_ok else "error",
                "source": "arxiv",
                "identifier": arxiv_id,
                "title": title,
                "confidence": 0.95,
            }
        else:
            result = {"status": "not_found", "source": "arxiv", "identifier": arxiv_id}
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, ET.ParseError, ValueError, TypeError) as e:
        result = {"status": "error", "source": "arxiv", "identifier": arxiv_id, "detail": str(e)[:100]}

    _cache_save(cache_key, result)
    return result


def verify_doi(doi: str, last_calls: dict[str, float], token: str | None = None) -> dict:
    """Verify a DOI via CrossRef API."""
    cache_key = _cache_key("doi", doi)
    cached = _cache_load(cache_key)
    if cached:
        return cached

    _delay("crossref", last_calls)
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    data = _req(url)
    if data and data.get("_http_status") == 404:
        result = {"status": "not_found", "source": "crossref", "identifier": doi}
    elif data and data.get("_request_error"):
        result = {
            "status": "error",
            "source": "crossref",
            "identifier": doi,
            "detail": data.get("_detail"),
        }
    elif data and data.get("status") == "ok":
        msg = data.get("message", {})
        if not isinstance(msg, dict):
            msg = {}
        title = None
        if msg.get("title"):
            title = msg["title"][0] if isinstance(msg["title"], list) else msg["title"]
        result = {
            "status": "verified" if isinstance(title, str) and title.strip() and str(msg.get("DOI", "")).lower() == doi.lower() else "error",
            "source": "crossref",
            "identifier": doi,
            "title": title,
            "container": msg.get("container-title", [None])[0] if msg.get("container-title") else None,
            "published": msg.get("published-print"),
            "confidence": 0.95,
        }
    else:
        result = {"status": "error", "source": "crossref", "identifier": doi, "detail": "unusable provider response"}

    _cache_save(cache_key, result)
    return result


def verify_ads(bibcode: str, last_calls: dict[str, float], token: str | None) -> dict:
    """Verify an ADS bibcode via the NASA ADS API."""
    # Basic token validation: must be present and at least 16 characters
    if not token or len(token.strip()) < 16:
        return {"status": "skipped", "source": "ads", "identifier": bibcode, "reason": "invalid_or_missing_ads_token"}

    cache_key = _cache_key("ads", bibcode)
    cached = _cache_load(cache_key)
    if cached:
        return cached

    _delay("ads", last_calls)
    params = urllib.parse.urlencode({"q": f'bibcode:"{bibcode}"', "fl": "title,bibcode,year,author,citation_count"})
    url = f"https://api.adsabs.harvard.edu/v1/search/query?{params}"
    headers = {"Authorization": f"Bearer {token}"}
    data = _req(url, headers=headers)
    if data and data.get("_request_error"):
        result = {
            "status": "error",
            "source": "ads",
            "identifier": bibcode,
            "detail": data.get("_detail"),
        }
    elif data and data.get("response", {}).get("numFound", 0) > 0:
        doc = data["response"]["docs"][0]
        result = {
            "status": "verified" if doc.get("bibcode") == bibcode and doc.get("title") else "error",
            "source": "ads",
            "identifier": bibcode,
            "title": doc.get("title", [None])[0] if doc.get("title") else None,
            "year": doc.get("year"),
            "authors": doc.get("author", []),
            "citation_count": doc.get("citation_count"),
            "confidence": 0.98,
        }
    else:
        result = {"status": "not_found", "source": "ads", "identifier": bibcode}

    _cache_save(cache_key, result)
    return result


def verify_title(title: str, last_calls: dict[str, float], token: str | None = None) -> dict:
    """Fallback: verify by title via OpenAlex."""
    cache_key = _cache_key("title", title.lower().strip()[:80])
    cached = _cache_load(cache_key)
    if cached:
        return cached

    _delay("openalex", last_calls)
    params = urllib.parse.urlencode({"search": title})
    url = f"https://api.openalex.org/works?{params}&per_page=3"
    data = _req(url)
    if data and data.get("_request_error"):
        result = {
            "status": "error",
            "source": "openalex",
            "identifier": title[:60],
            "detail": data.get("_detail"),
        }
    elif data and data.get("meta", {}).get("count", 0) > 0:
        best = data["results"][0]
        # Jaccard-like similarity on title words
        title_words = set(title.lower().split())
        best_words = set((best.get("title") or "").lower().split())
        overlap = len(title_words & best_words)
        jaccard = overlap / max(len(title_words | best_words), 1)
        result = {
            "status": "low_confidence",
            "source": "openalex",
            "identifier": title[:60],
            "matched_title": best.get("title"),
            "doi": best.get("doi"),
            "jaccard_score": round(jaccard, 3),
            "confidence": round(jaccard * 0.9, 2),  # discount vs. direct API
        }
    else:
        result = {"status": "not_found", "source": "openalex", "identifier": title[:60]}

    _cache_save(cache_key, result)
    return result


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def verify_citation(
    identifier: str,
    id_type: str | None,
    last_calls: dict[str, float],
    ads_token: str | None = None,
    title_fallback: str | None = None,
) -> dict:
    """Route a single citation to the correct verifier based on id_type.

    Args:
        identifier: The raw identifier string (arxiv ID, DOI, bibcode, or title).
        id_type: One of 'arxiv', 'doi', 'ads', 'title', or None for auto-detect.
        last_calls: Timestamp tracker for rate limiting.
        ads_token: NASA ADS API token.
        title_fallback: If primary lookup fails, try title match.

    Returns:
        Verification result dict.
    """
    # Clean and route arXiv identifiers
    clean_identifier = identifier
    # Use .search() instead of .match() to find the ID anywhere in the string
    arxiv_match = RE_ARXIV.search(identifier)
    if arxiv_match:
        clean_identifier = arxiv_match.group(1)
        id_type = "arxiv"
    elif RE_ARXIV_BARE.match(identifier):
        clean_identifier = identifier
        id_type = "arxiv"
    elif id_type is None or id_type == "auto":
        if RE_DOI.match(identifier):
            id_type = "doi"
        elif RE_ADS.match(identifier) and len(identifier) > 10:
            id_type = "ads"
        else:
            id_type = "title"

    result = None
    if id_type == "arxiv":
        result = verify_arxiv(clean_identifier, last_calls, ads_token)
    elif id_type == "doi":
        doi_match = RE_DOI.search(identifier)
        result = verify_doi(doi_match.group(1) if doi_match else identifier, last_calls, ads_token)
    elif id_type == "ads":
        result = verify_ads(identifier, last_calls, ads_token)
    elif id_type == "title":
        result = verify_title(identifier, last_calls, ads_token)

    # Title discovery never overrides a failed identifier or verifies its identity.
    if result and result.get("status") in ("not_found", "error") and title_fallback:
        fallback = verify_title(title_fallback, last_calls, ads_token)
        fallback["primary_lookup"] = result
        fallback["status"] = "low_confidence"
        fallback["note"] = f"Primary {id_type} lookup failed; title candidate needs manual resolution"
        return fallback

    return result or {"status": "error", "identifier": identifier, "note": "no_verifier_matched"}


def batch_verify(
    citations: list[dict],
    ads_token: str | None = None,
    timeout: int = GLOBAL_TIMEOUT,
) -> dict:
    """Run verification across a list of citations.

    Each citation dict can have:
        - id: the identifier string
        - type: 'arxiv'|'doi'|'ads'|'title'|None (auto-detect)
        - title: optional fallback title
        - label: optional human-readable label

    Returns a VerificationReport (dict with summary + per-citation results).
    """
    start = time.time()
    last_calls: dict[str, float] = defaultdict(float)
    results = []
    stats = {"total": len(citations), "verified": 0, "low_confidence": 0, "mismatch": 0, "not_found": 0, "error": 0, "skipped": 0}

    for i, cit in enumerate(citations):
        elapsed = time.time() - start
        if elapsed > timeout:
            for pending in citations[i:]:
                results.append({"status": "skipped", "identifier": pending.get("id", ""), "reason": "batch_timeout"})
                stats["skipped"] += 1
            break

        identifier = cit.get("id", "")
        id_type = cit.get("type")
        title_fallback = cit.get("title")
        expected_title = cit.get("expected_title")
        label = cit.get("label", identifier)

        result = dict(verify_citation(identifier, id_type, last_calls, ads_token, title_fallback))
        actual_title = result.get("title") or result.get("matched_title")
        if result.get("status") == "verified" and expected_title and not actual_title:
            result["status"] = "error"
            result["note"] = "Expected title could not be checked against missing metadata"
        if result.get("status") == "verified" and expected_title and actual_title:
            title_score = _title_similarity(expected_title, actual_title)
            result["expected_title"] = expected_title
            result["title_match_score"] = round(title_score, 3)
            if title_score < 0.8:
                result["status"] = "mismatch"
                result["note"] = "Identifier resolved, but title does not match expected work"
        result["label"] = label
        results.append(result)

        s = result.get("status", "error")
        if s == "verified":
            stats["verified"] += 1
        elif s == "low_confidence":
            stats["low_confidence"] += 1
        elif s == "mismatch":
            stats["mismatch"] += 1
        elif s == "not_found":
            stats["not_found"] += 1
        elif s == "error":
            stats["error"] += 1
        elif s == "skipped":
            stats["skipped"] += 1

    report = {
        "report_type": "VerificationReport",
        "generated_at": datetime.now().isoformat(),
        "stats": stats,
        "citations": results,
        "config": {
            "ads_configured": ads_token is not None,
            "cache_enabled": True,
        },
    }
    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _extract_citations(text: str) -> list[dict]:
    """Parse a text blob for arXiv IDs, DOIs, and ADS bibcodes."""
    citations = []
    seen = set()

    for m in RE_ARXIV.finditer(text):
        raw = m.group(1)
        if raw not in seen:
            seen.add(raw)
            citations.append({"id": raw, "type": "arxiv", "label": f"arXiv:{raw}"})

    for m in RE_DOI.finditer(text):
        raw = m.group(1).rstrip(".")
        if raw not in seen:
            seen.add(raw)
            citations.append({"id": raw, "type": "doi", "label": f"DOI:{raw}"})

    # Loose bibcode detection
    for line in text.splitlines():
        for word in line.split():
            word = word.strip(",. ;:!?")
            if word not in seen and len(word) >= 10 and word[0].isdigit():
                # Heuristic: starts with digit-year, contains letters
                if sum(1 for c in word if c.isalpha()) >= 4:
                    seen.add(word)
                    citations.append({"id": word, "type": "ads", "label": word})

    return citations



def main():
    parser = argparse.ArgumentParser(description="MVF Citation Verification Framework")
    parser.add_argument("--input", help="JSON file with list of citation dicts")
    parser.add_argument("--output", help="Write VerificationReport to this JSON path")
    parser.add_argument("--summary", action="store_true", help="Print a human-readable summary")
    parser.add_argument("--extract", help="Extract citations from a text file and verify")
    parser.add_argument("--raw", action="store_true", help="Print the raw JSON report to stdout")
    parser.add_argument("--cache-dir", type=Path, help="Local cache directory; do not publish cache contents")
    args = parser.parse_args()
    global CACHE_DIR
    if args.cache_dir is not None:
        CACHE_DIR = args.cache_dir

    ads_token = os.environ.get("ADS_API_TOKEN")

    # Source citations
    citations = []
    if args.extract:
        text = Path(args.extract).read_text()
        citations = _extract_citations(text)
        print(f"Extracted {len(citations)} citations from {args.extract}")
    elif args.input:
        citations = json.loads(Path(args.input).read_text())
    else:
        parser.error("supply --input or --extract; no implicit live citation batch")

    # Run verification
    report = batch_verify(citations, ads_token=ads_token)
    stats = report["stats"]

    # Output
    output_path = args.output
    if output_path:
        Path(output_path).write_text(json.dumps(report, indent=2))
        print(f"\nReport written to: {output_path}")

    if args.summary or not output_path:
        print(f"\n{'='*60}")
        print(f"  MVF Verification Report")
        print(f"  Generated: {report['generated_at']}")
        print(f"{'='*60}")
        print(f"  Total checked:   {stats['total']}")
        print(f"  ✅ Verified:      {stats['verified']}")
        print(f"  Advisory only:   {stats['low_confidence']}")
        print(f"  🔎 Mismatch:      {stats['mismatch']}")
        print(f"  ❌ Not found:     {stats['not_found']}")
        print(f"  ⚠️  Errors:       {stats['error']}")
        print(f"  ⏭️  Skipped:      {stats['skipped']}")
        print(f"  ADS API:         {'✅ Configured' if report['config']['ads_configured'] else '❌ Token missing'}")
        print(f"{'='*60}")
        print("  Cache: local; contents and path omitted from report")
        print(f"{'='*60}\n")

        if _MVF_LOGS:
            print(f"  Diagnostic Logs ({len(_MVF_LOGS)} entries):")
            for log in _MVF_LOGS:
                print(f"    - {log}")
            print()

        for cit in report["citations"]:
            label = cit.get("label", cit["identifier"])
            status_icon = {
                "verified": "✅",
                "low_confidence": "⚠️",
                "mismatch": "🔎",
                "not_found": "❌",
                "error": "💥",
                "skipped": "⏭️",
            }.get(cit.get("status", "error"), "❓")
            source = cit.get("source", "?")
            conf = cit.get("confidence", "")
            conf_str = f" (conf={conf})" if isinstance(conf, float) else ""
            print(f"  {status_icon} [{source:>8}] {label}{conf_str}")

    if args.raw:
        print(f"\n--- RAW REPORT ---\n{json.dumps(report, indent=2)}")
    return 0 if stats["total"] > 0 and stats["verified"] == stats["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
