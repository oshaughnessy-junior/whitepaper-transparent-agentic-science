---
name: records-protocol
description: Place scientific evidence, decisions and retractions in durable records without bloating code. Use for scientific PRs, notes, code comments, negative results and archival test decisions.
---

# Records protocol

Identify the existing owning paper/research note and code repository. Link their records instead of inventing a parallel archive. The project supplies its own storage map; this skill contains no private repository mappings or host paths.

| Content | Durable home | What code retains |
|---|---|---|
| Measurements, convergence tables, failed approaches | Owning research note or versioned design record | Concise decision and evidence pointer |
| Scientific interpretation and its limits | Research synthesis, then supported paper claims | Implementation constraints |
| Units, conventions and ordering requirements | Code/API contract | Short present-tense explanation |
| Reproduction commands and environment | Artifact README and run manifest | Entry point/backlink |
| Review findings and dispositions | Versioned review record linked from the synthesis | Regression for a supported repair |
| Retraction | Originating note plus downstream consistency sweep | Remove superseded advice; keep valid constraints |

PR discussions communicate review but must not be the sole home of a durable measurement or negative result. Link the record needed to reproduce the decision. Restrict private records appropriately and keep public summaries useful without inaccessible details.

During development, mark temporary explanatory scaffolding. Before merge, delete it, promote its evidence to a durable note, or distill a real invariant into a concise code comment. Do not erase the evidence behind an inconvenient result. Retain a named, tested decision constant where relevant; a dated record alone cannot prevent staleness.

Distinguish invariant tests from archival reproductions. Invariants track conventions, mechanisms and boundary behavior through legitimate changes. Archival tests freeze the paper's inputs, configuration and tolerances; a mismatch after code evolution is information to investigate, not permission to change the expected value. Link both to evidence.

When a result changes, search all dependent claims: notes, code guidance, help/error text, plots, macros, captions and paper conclusions. Check for absence of superseded advice as well as presence of the new advice. Record which artifact governs current behavior and which preserves historical evidence. See ../result-provenance and ../autonomous-science.
