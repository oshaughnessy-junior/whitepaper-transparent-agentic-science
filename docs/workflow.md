# Research procedure

The PRD-style paper/main.tex is the scientific entry point. The prior operational note is preserved as paper/main_for_agents.tex; this file is the operational contract.

1. Define the question, scientific domain, units, assumptions, data selection, acceptance criteria, and failure cases before expensive runs. Assign stable claim IDs.
2. Pilot the actual production entry point. Establish runtime and memory needs before scaling. Confirm important configuration switches change the intended observable.
3. Record input hashes, code revisions including local modifications, environment and hardware, command/configuration, seeds, job and host, output checksums, and termination status. A submitted or running job supplies no result.
4. Validate against analytic answers, limiting cases, independent implementations, multiple seeds, convergence studies, and held-out inputs. Show that a deliberately broken candidate fails. Report the domain of agreement and shared assumptions.
5. Integrate the result into durable scientific notes: question, derivation, evidence, uncertainty, interpretation, limitations, verdict. Logs and dated checkpoints support these notes.
6. Challenge substantive candidates with independent science and code/numerics reviews. Pin the candidate and scientific specification. Record reviewer exposure, reference lineage, commands, findings, dispositions, and rechecks. Self-review is labeled self-review.
7. Promote a result only after claim-specific gates pass: completed evidence, convergence, reproducibility, boundary checks, identifiability where relevant, Monte Carlo error, predictive tests in the observable domain, and provenance. Keep unsupported results provisional.
8. Generate macros, tables, and figure labels from one result artifact. Repeated quantities use the same result key and presentation convention. Related papers discussing the same quantity share the artifact or regenerate from exactly the same pinned record.
9. Write the paper by claim. The human supplies the scientific thesis, structure, audience, and claim strength. Develop equations before implementation details; use evidence-bearing figures. Keep run chronology in notes. Audit semantic changes after prose editing.
10. When a claim fails, preserve the objection, mark the claim retracted or narrowed, add the killing test, and sweep every dependent abstract, caption, table, conclusion, companion paper, and note. Preserve frozen historical results with their explicit domain.
11. Rebuild and inspect the final document and submission source. Resolve citations against records and read the supporting passage. Produce a source archive and verify its rendered output. Obtain human scientific sign-off and author consent before submission.

## Numerical consistency boundary

The runnable tooling case uses an intentionally narrow source contract: all manuscript source is paper/main.tex plus generated fragments; computed result literals occur only in generated files. `make check` regenerates into a temporary directory and compares bytes, checks named uses, and rejects unregistered bare numeric literals in the manuscript. The current exact exceptions are the date command, hyperlink URL targets, checked citation identifiers, the exact approved REVTeX class declaration, bibliographic metadata, and the exact integral specification. Citation keys are checked for missing and duplicate definitions; source identity and relevance require separate retrieval checks. The exception registry must be reviewed as evidence, not used to hide results.

This prevents transcription drift within that contract. It does not establish that the input data, selected result key, estimator, units, or scientific interpretation are correct. General TeX is programmable; unrestricted includes, dynamically constructed macros, manually drawn labels, and externally edited figures would need broader tooling and review. Do not describe this small checker as a general proof of manuscript consistency.

## Code validation beyond unit tests

- **Paper examples:** rerun documented demonstrations and representative analyses; regenerate the observables, figures and tables supporting the manuscript.
- **Previous codes:** compare new and earlier released implementations at matched input, convention, configuration and accuracy. Record intentional corrections; never restore a known defect merely to match a baseline.
- **Literature benchmarks:** identify the published calculation and error budget, reproduce its assumptions, and record shared dependencies that limit independence.
- **Production environment:** test the installed executable, normal launcher/configuration, target CPU/GPU backend, dependency stack and scheduler with representative inputs. Include an end-to-end case; archive larger campaigns separately when they do not fit CI.
- **Regression evidence:** retain a small executable version of a diagnosed failure in CI where practical, plus negative controls, collection counts, skip reasons and exact candidate identity.

## Figure and repository provenance

Every figure, including a diagnostic, points to its regeneration recipe. A source comment and linked sidecar identify data releases/hashes, effective cuts/settings, units/normalization, transformations, script/build target, code/environment identity, plotted data and final artifact. Captions explain the scientific content and provide a concise provenance pointer. State separately how to replot saved data and how to rerun the underlying analysis.

Every owning repository provides input acquisition/access/license instructions, a pinned environment, run and verification commands, expected outputs, and links to reviewed revisions, CI receipts and any external output archive. Restricted or missing inputs remain explicit reproduction limits.

The synthetic source checker accepts only the declared braced `input`/`include` grammar, including whitespace/comment separation. It rejects unregistered paths, unbraced includes and conditional file-inclusion commands. This is an intentionally restricted contract, not a general TeX parser or proof about arbitrary TeX.
