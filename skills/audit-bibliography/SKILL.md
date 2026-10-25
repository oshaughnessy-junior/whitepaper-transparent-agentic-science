---
name: audit-bibliography
description: Audit BibTeX or extracted reference lists for identifier and metadata mismatches. Use for bibliography verification and reference CI gates, separately from semantic claim support.
---

# Audit bibliography

Verify bibliography identity and metadata; use ../cite-and-verify separately to check whether the source supports the attached prose.

From this skill's directory:

```bash
python3 scripts/validate_refs.py refs.bib --profile astronomy
python3 scripts/validate_refs.py refs.bib --style off
python3 -m unittest discover -s tests -v
```

The astronomy profile handles ADS bibcodes, collaboration authors and whole-title bracing. Set ADS_API_TOKEN through the environment when needed. BIB_AUDIT_MAILTO and S2_API_KEY are optional environment configuration, never command-line secrets. Send only shareable identifiers or search terms to external metadata services; a private reference list may itself reveal a research direction. Read references/astronomy-policy.md for authority/formatting rules and references/metadata-apis.md for the request boundary.

Prefer .bib/.bbl or publisher sources. For PDF-only references, extract text, construct structured JSON without invented identifiers, confirm the count, then run scripts/audit_refs.py. The heuristic resolve_refs.py path is an advisory fallback; bad splitting can manufacture accusations.

P1/P2 identity findings produce a failing command; metadata drift and style are advisory. An API error is unresolved lookup, not proof of fabrication. Confirm alleged absence manually. A successful exit is insufficient if required queries were skipped, failed or unsupported: inspect coverage and resolve those gaps. Run a syntax/datamodel checker separately when the project requires one.

These stdlib regression tests exercise metadata/parser logic using offline records. They do not certify current API availability, every live bibliography, or scientific support. Preserve UPSTREAM_LICENSE and references/provenance.md when redistributing.
