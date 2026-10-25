# Claim ledger

The bundled schema retains the source format identifier openclaw.claim-ledger.v1 for compatibility; no OpenClaw runtime is required. An example is in ../examples/claim-ledger.json.

Each claim records id, exact claim, claim_type, consequence_level, identity_status, support_status, disposition, reviewer, and human_required. A verified claim also requires sources, a source_locator and an evidence note. A human-asserted claim names human_verifier; it remains attributed testimony, distinct from independent source verification. Blocked medium/high claims require an explicit human decision before promotion.

The validator checks declared structure and consistency. It cannot prove that a source was read, that the evidence note is accurate, or that the claimed implication is valid. Use strong semantic review for consequential claims. Preserve prior objections when revising dispositions.
