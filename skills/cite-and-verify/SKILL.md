---
name: cite-and-verify
description: Verify source identity and the support for consequential scientific claims. Use for references, attribution, evidence packets and manuscript claim audits.
---

# Cite and verify

Use two gates. A resolving identifier establishes neither relevance nor support for a sentence.

## Source identity

Run from this skill's directory:

```bash
python3 scripts/citation_mvf.py --input citations.json --output identity-report.json --summary
```

Each input entry has `id`, `type` (`doi`, `arxiv`, `ads`, or `title`) and, when known, `expected_title`. Use explicit input; there is no default live batch. DOI/arXiv/ADS metadata can verify identity; title search is advisory. Missing ADS credentials, provider errors, unprocessed work and title-only matches remain unresolved. The command returns nonzero unless every requested entry verifies. Set ADS_API_TOKEN through the environment; do not put credentials in command arguments, reports or fixtures.

The service receives supplied identifiers/search terms. Send only public-source queries; do not submit private manuscript text through `--extract`. Cache and report files can contain source selections and belong in a local project-controlled location until reviewed for publication. Use `--cache-dir` to choose a project cache; no cache or query history is bundled with this skill.

## Claim support

For every consequential claim record its exact wording, source identity result, source locator, short evidence note, supported scope and disposition. Read the source rather than treating a generated summary as evidence. A verified identity is only the first gate.

Use one claim ledger for the artifact and validate it:

```bash
python3 scripts/validate_claim_ledger.py claim-ledger.json
```

See references/claim-ledger-schema.md and examples/claim-ledger.json. `verified` requires source identity plus semantic support. `human-asserted` attributes an explicit human statement; it is not independent verification. `blocked` covers missing, partial or conflicting support. Keep blocked consequential claims out of final prose until resolved; do not invent a stronger interpretation. The validator checks structure and declared consistency, not whether a source was actually read or supports the claim.

Use ../audit-bibliography for structured BibTeX and metadata diagnostics. Use ../science-editing for bounded wording changes; a citation acquiring a new burden requires a renewed support check.
