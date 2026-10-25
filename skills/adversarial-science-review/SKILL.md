---
name: adversarial-science-review
description: Review a pinned scientific claim with separate science and numerics challenges, exposure records, and preserved finding dispositions. Use for substantive scientific review, not ordinary prose polishing.
---

# Adversarial Science Review

Pin the scientific specification and candidate commit or content hash. Provide domain, units, assumptions, raw evidence, resources, and acceptance conditions. Withhold implementer advocacy and other reviewers\' conclusions during the first pass. Record exactly what each reviewer saw.

Where authorized and available, use separate fresh contexts for science and code/numerics review. The science reviewer derives a load-bearing result or hunts a counterexample, missing physics, selection effect, or unjustified claim. The numerics reviewer traces the production path, reproduces relevant checks, probes conditioning/boundaries, and demonstrates an isolated wrong candidate can fail. If independent execution is unavailable, label self-review and keep the independent gate pending.

Record reviewer identity, candidate, reference lineage, exposure, commands/derivations, findings, severity, domain and verdict. A different model does not establish independence. A reviewer who repairs the candidate becomes an implementer for that repair; obtain fresh review of the changed candidate.

Preserve every objection and disposition: repaired with recheck, claim narrowed, rejected with contrary evidence, or unresolved. Re-review affected claims after material changes. A timeout or inconclusive check is not acceptance. End as accepted in a named domain, provisional, refuted, or blocked. See ../../PROVENANCE.md for method attribution and ../../docs/workflow.md for claim retraction.

For sustained investigations, ../autonomous-science supplies the research cycle and independence ledger; ../records-protocol places findings and retractions in durable records. Check the relevance of benchmark proxies and swept domains as well as arithmetic. A comparison with mature code begins by checking the harness and conventions, while still allowing a demonstrated defect in either implementation.
