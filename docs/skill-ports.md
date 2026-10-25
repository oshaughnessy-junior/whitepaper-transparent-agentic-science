# Portable science skill additions

The user authorized essential ports that avoid releasing private information. The resulting bundle has **nine skills**: the original four, five focused additions, and supporting executable tools. The recommendation-stage inventory remains in skill-port-assessment.md; this document records what was actually implemented.

## Included

| Package | Delivered scope |
|---|---|
| cite-and-verify | Identifier/title checks; advisory title searches; separate semantic-support ledger, schema, validator and synthetic example |
| audit-bibliography | BibTeX/reference metadata auditing, astronomy profile, MIT upstream notice and offline regressions |
| science-editing | Bounded editing contract, semantic freeze, redline validation, edit ledger and synthetic behavioral canaries |
| autonomous-science | Bounded research cycle, independent review contract, ownership, synthesis, resource/permission boundaries and resumable checkpoints |
| records-protocol | Durable record routing, negative findings/retractions, concise code constraints and archival versus invariant tests |
| result-provenance, extended | General scalar/interval logger adapted from maintained research-skills, with required completed-run metadata, producer hashes, namespaced TeX results and generated-byte checks |
| Existing review/validation/writing skills | Cross-links and selected evidence-discipline, environment isolation and writing-packet practices, avoiding competing umbrella procedures |

The source is the user's agent-skills repository, with result logging taken from the maintained research-skills implementation rather than its deprecated snapshot. The new procedure texts are portable adaptations. Bibliography scripts/tests, citation scripts and logger were selectively adapted; no repository history or whole source tree was imported.

## Publication boundary

Excluded: source project maps, named private record stores, raw memories, operational transcripts, host paths, credentials, local caches, deployment/runtime configuration, unpublished numerical anecdotes and private source revision identifiers. Selected source files were scanned for these categories. Tests use public bibliographic examples, supplied metadata or clearly synthetic records; real credentials and private research queries were not used.

No private runtime data is needed to use the public skills. Citation services receive the identifiers/search terms supplied by the operator. This is an explicit data-flow boundary: do not send restricted text or queries simply because a script can extract them. Generated run manifests and identity reports can themselves reveal private work; review them before publication rather than exporting them automatically.

Preserved Isaac Corley's MIT upstream notice for audit-bibliography and its public upstream provenance. Local procedure adaptations use the repository's CC BY 4.0 terms and locally owned executable adaptations use MIT, as recorded in NOTICE.md. Autonomous-science retains attributed BootLoops method lineage; no BootLoops implementation was copied. Private source ownership is not presented as an upstream open-source license.

## Strengthening done during porting

- Removed command-line credential input and the inherited implicit live citation batch. Missing credentials, API failures, unprocessed requests and title-only matches cannot produce a successful citation gate.
- Added direct returned-identifier and expected-title checks, encoded ADS bibcodes, and versioned cache invalidation so older verification semantics do not silently survive a stricter gate.
- Replaced substring-based credential routing with exact HTTPS host/port checks. Credential-bearing redirects are refused in both bibliography and citation helpers. Query text containing a provider name cannot select a credential destination.
- Strengthened ledger checks for empty/duplicate entries, blank evidence/source fields and named human attribution. Semantic support still requires actual reading; a structural validator cannot establish it.
- Removed the logger's arbitrary display override. Display derives from raw scalar/interval values, stated rounding and trusted units. Namespaced result keys preserve existing math commands. Required completed-run metadata and producer/input identities prevent incomplete declarations from being accepted as ready records.
- Expanded supported explicit result-use checks to whitespace/comment variants and rejected unsupported syntax. This is a limited trusted-source interface, not a general TeX proof or sandbox.

## Validation and limits

`make check` runs both root and bibliography suites, including actual command-line paths and negative controls. The root suite covers citation errors, title/identifier mismatches, missing credentials, cache versioning, semantic-ledger declarations, generated corruption, undefined result uses and required run metadata. Bibliography regressions cover identity/parser false accusations and credential destination/redirect handling. Provider responses are mocked for these tests; live scholarly APIs were not exercised for this port.

All nine SKILL.md files passed the skill-creator structural validator. A synthetic result named Lambda was also built with local pdflatex: the document retained the standard math Lambda and displayed the namespaced result. The built-in compiler checks the updated main document; PDF export remains a draft, not a submission.

An independent subagent challenged the ports using synthetic temporary inputs and offline transport. Its findings and dispositions are preserved in reviews/skill-ports-review.md. That review is bounded source/behavioral evidence, not a guarantee of every future input, remote API response, or scientific conclusion.

The general logger checks required declared provenance and consistency with generated TeX. It does not independently establish job completion, rehash unavailable remote inputs, serialize multiple writers, certify physics or traverse arbitrary included TeX. Use one writer per shared record or external serialization. Keep a clean regeneration check tied to the actual analysis and retain scientific review.
