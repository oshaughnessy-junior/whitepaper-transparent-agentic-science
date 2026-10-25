#!/usr/bin/env python3
"""Validate the minimal structure and policy invariants of a claim ledger."""

import argparse
import json
import sys
from pathlib import Path

ALLOWED_CLAIM_TYPES = {"fact", "number", "attribution", "interpretation", "recommendation"}
ALLOWED_CONSEQUENCE_LEVELS = {"low", "medium", "high"}
ALLOWED_IDENTITY_STATUSES = {"verified", "low-confidence", "not-found", "error", "skipped", "not-applicable"}
ALLOWED_SUPPORT_STATUSES = {"supported", "partial", "unsupported", "human-verified"}
ALLOWED_DISPOSITIONS = {"verified", "human-asserted", "blocked"}


def _require(record, field, errors, index):
    if field not in record or record[field] in (None, "", []):
        errors.append(f"claims[{index}].{field}: required")


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["root: expected object"]
    if data.get("schema") != "openclaw.claim-ledger.v1":
        errors.append("schema: expected openclaw.claim-ledger.v1")
    if not isinstance(data.get("claims"), list):
        return errors + ["claims: expected array"]

    if not data["claims"]:
        errors.append("claims: empty ledger does not certify an artifact")
    seen = set()
    for index, claim in enumerate(data["claims"]):
        if not isinstance(claim, dict):
            errors.append(f"claims[{index}]: expected object")
            continue
        for field in ("id", "claim", "claim_type", "consequence_level", "identity_status",
                      "support_status", "disposition", "reviewer", "human_required"):
            _require(claim, field, errors, index)
        if claim.get("claim_type") not in ALLOWED_CLAIM_TYPES:
            errors.append(f"claims[{index}].claim_type: invalid value")
        if claim.get("consequence_level") not in ALLOWED_CONSEQUENCE_LEVELS:
            errors.append(f"claims[{index}].consequence_level: invalid value")
        if claim.get("identity_status") not in ALLOWED_IDENTITY_STATUSES:
            errors.append(f"claims[{index}].identity_status: invalid value")
        if claim.get("support_status") not in ALLOWED_SUPPORT_STATUSES:
            errors.append(f"claims[{index}].support_status: invalid value")
        if claim.get("disposition") not in ALLOWED_DISPOSITIONS:
            errors.append(f"claims[{index}].disposition: invalid value")

        for field in ("id", "claim", "reviewer"):
            if not isinstance(claim.get(field), str) or not claim[field].strip():
                errors.append(f"claims[{index}].{field}: nonempty string required")
        if not isinstance(claim.get("human_required"), bool):
            errors.append(f"claims[{index}].human_required: expected boolean")
        key = claim.get("id")
        if isinstance(key, str):
            if key in seen:
                errors.append(f"claims[{index}].id: duplicate")
            seen.add(key)
        else:
            errors.append(f"claims[{index}].id: expected string")
        disposition = claim.get("disposition")
        support = claim.get("support_status")
        identity = claim.get("identity_status")
        if disposition == "verified":
            if not isinstance(claim.get("sources"), list) or not claim["sources"] or any(not isinstance(source, str) or not source.strip() for source in claim["sources"]):
                errors.append(f"claims[{index}].sources: nonempty array required")
            if identity != "verified":
                errors.append(f"claims[{index}]: verified disposition requires verified identity")
            if support != "supported":
                errors.append(f"claims[{index}]: verified disposition requires supported claim")
            for field in ("source_locator", "evidence"):
                if not isinstance(claim.get(field), str) or not claim[field].strip():
                    errors.append(f"claims[{index}].{field}: nonempty string required")
        elif disposition == "human-asserted":
            if support != "human-verified":
                errors.append(f"claims[{index}]: human-asserted requires human-verified support")
            if not isinstance(claim.get("human_verifier"), str) or not claim["human_verifier"].strip():
                errors.append(f"claims[{index}].human_verifier: nonempty string required")
        elif disposition == "blocked" and claim.get("consequence_level") in {"medium", "high"}:
            if claim.get("human_required") is not True:
                errors.append(f"claims[{index}]: blocked consequential claim requires human_required=true")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", help="Path to claim-ledger JSON")
    args = parser.parse_args()
    path = Path(args.ledger)
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 1
    errors = validate(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {len(data['claims'])} claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())

