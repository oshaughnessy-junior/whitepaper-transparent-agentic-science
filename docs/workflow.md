# Research procedure

The technical note is the narrative entry point; this file is the operational contract.

1. Define the question, scientific domain, units, assumptions, data selection, acceptance criteria, and failure cases before expensive runs. Assign stable claim IDs.
2. Pilot the actual production entry point. Establish runtime and memory needs before scaling. Confirm important configuration switches change the intended observable.
3. Record input hashes, code revisions including local modifications, environment and hardware, command/configuration, seeds, job and host, output checksums, and termination status. A submitted or running job supplies no result.
4. Validate against analytic answers, limiting cases, independent implementations, multiple seeds, convergence studies, and held-out inputs. Show that a deliberately broken candidate fails. Report the domain of agreement and shared assumptions.
5. Integrate the result into durable scientific notes: question, derivation, evidence, uncertainty, interpretation, limitations, verdict. Logs and dated checkpoints support these notes.
6. Challenge substantive candidates with independent science and code/numerics reviews. Pin the candidate and scientific specification. Record reviewer exposure, reference lineage, commands, findings, dispositions, and rechecks. Self-review is labeled self-review.
7. Promote a result only after claim-specific gates pass: completed evidence, convergence, reproducibility, boundary checks, identifiability where relevant, Monte Carlo error, predictive tests in the observable domain, and provenance. Keep unsupported results provisional.
8. Generate macros, tables, and figure labels from one result artifact. Repeated quantities use the same result key and presentation convention. Both companion papers share the artifact or regenerate from exactly the same pinned record.
9. Write the paper by claim. The human supplies the scientific thesis, structure, audience, and claim strength. Develop equations before implementation details; use evidence-bearing figures. Keep run chronology in notes. Audit semantic changes after prose editing.
10. When a claim fails, preserve the objection, mark the claim retracted or narrowed, add the killing test, and sweep every dependent abstract, caption, table, conclusion, companion paper, and note. Preserve frozen historical results with their explicit domain.
11. Rebuild and inspect the final document and submission source. Resolve citations against records and read the supporting passage. Produce a source archive and verify its rendered output. Obtain human scientific sign-off and author consent before submission.

## Numerical consistency boundary

The runnable tooling case uses an intentionally narrow source contract: all manuscript source is paper/main.tex plus generated fragments; computed result literals occur only in generated files. `make check` regenerates into a temporary directory and compares bytes, checks named uses, and rejects unregistered bare numeric literals in the manuscript. The current exact exceptions are the date command, hyperlink URL targets, the companion manuscript directory identifier, and the exact integral specification. The exception registry must be reviewed as evidence, not used to hide results.

This prevents transcription drift within that contract. It does not establish that the input data, selected result key, estimator, units, or scientific interpretation are correct. General TeX is programmable; unrestricted includes, dynamically constructed macros, manually drawn labels, and externally edited figures would need broader tooling and review. Do not describe this small checker as a general proof of manuscript consistency.
