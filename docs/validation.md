# Initial validation record

Date: 2026-10-23. Executor: OpenAI Codex (AI agent).

- `make check`: passed; nine tests collected and passed. The cases exercise clean regeneration, corrupted artifacts, changed input, changed producer identity, undefined result, typed result, untracked include, deliberately wrong numerical result, and expected refinement behavior. The corrupted-artifact case checks all generated products.
- Four portable skill packages passed the bundled skill-creator frontmatter/scaffold validator after final edits. This is structural validation, not behavioral certification.
- `paper/main.tex`: compiled successfully with the Codex desktop editor compiler after final edits. The existing editor was preserved. No separate PDF was created by this task. Rendered visual inspection is not claimed.
- Cardassia inspection was read-only. Project memory, selected run-side documents, and corrective commit descriptions were inspected. No scientific job was launched and no source repository was modified.
- Independent reviewer pass: pending at initial release; a later scoped review is recorded below. The authoring agent's checks are self-verification.
- Full reruns of the two scientific manuscripts: pending.
- `make submission`: prepared as a source-bundle recipe but not executed; archive compilation and rendered comparison remain pending. This recipe is not a submission authorization.
- Current official arXiv submission overview and relevant passages in the posted methods-paper HTML were read. A complete release bibliography/attribution audit remains pending.

A source pointer from project memory was absent at the remembered checkout. It is recorded as a path-recovery gap rather than a verified reproduction command. See cardassia-lessons.md.

The public edition excludes private source hashes, memory filenames, host paths and corrective-history identifiers. Detailed source audit records were retained outside this repository.

## PRD-style revision

- Preserved the operational draft as `paper/main_for_agents.tex`, with the scientific-example scope corrected.
- Rebuilt `paper/main.tex` as a REVTeX 4.2 PRD reprint article for scientific readers. The main examples are the main papers in `popsynth_hyperpipe_paper` and `gwk-hierarchical-initial`; source links are marked as access-restricted.
- Read the official Physical Review/APS, ApJ/AAS and arXiv AI guidance. `docs/policy-sources.md` records their URLs and scope. The introduction cites those policies; it does not repeat unverified penalty claims from inherited instructions.
- Updated the numerical checker for the approved REVTeX declaration and bibliographic metadata. Added undefined/duplicate citation-key failure checks; these do not certify literature relevance.
- `make check`: all eleven tests passed. `git diff --check`: passed. Ancillary-paper identifier sweep: no matches in the current tree.
- The revised main source compiled successfully with the Codex desktop compiler. The existing editor was retained; no separate PDF was generated. Visual layout inspection and final human approval remain separate checks.

## Capability baseline and concrete bug-finding revision

- Added the human-specified convention: latest available OpenAI model at Sol scale, or comparable Claude Opus capability, unless otherwise noted; comparable capability is recommended for scientific work.
- Stated the human's developer/operator assessment that adversarial review at this capability already matches or exceeds typical human performance at finding and diagnosing errors in ordinary scientific workflows. This is an operational assessment supported by multiple project examples, not a newly measured comparative benchmark.
- Expanded the reliability discussion with solver comparison, interface/caller audits, stale-cache diagnosis, run-to-manuscript tracing, and the recorded sample-identity and launcher-configuration cases.
- Added a verified public source describing AI-generated fuzz tests finding previously unknown defects in mature, extensively tested software. No private source identifiers or raw project memory were added.
- Numerical/citation consistency check and `git diff --check` passed. The final main source compiled successfully with the desktop editor compiler; no separate PDF was generated.

## RIFT review-sequence evidence

- Read metadata and descriptions for the merged RIFT PRs 234, 266 and 459 through the GitHub connector. Added direct access-restricted links and qualitative failure mechanisms; no private commit hashes or run locations are exported.
- Checked the main third-generation RIFT title and author list against the source and the public arXiv record, 2609.37393. It is cited as a posted preprint, not as an unpublished forthcoming paper. Follow-on studies remain future work; later PRs are not attributed automatically to that preprint version.
- Added the evidence inventory in cases/README.md. Underlying RIFT numerical campaigns were not rerun here. No quantitative PR results were transcribed into manuscript prose.
- Numerical/citation consistency check and whitespace validation passed. The final main source compiled successfully in the existing desktop editor.

## Human-facing tightening and adversarial review

- Tightened the note with selective boldface and lists, foregrounding adversarial review, CI for code, and reproducible provenance for every result, figure, and repository. Added explicit validation against paper examples, previous released codes, literature benchmarks, and the installed production execution path. Updated the portable simulation-validation skill accordingly.
- Inspected NuclearMatter-Backend development records and read-only project lessons on CIT, cardassia, and sporc. The case inventory links dated public solver/interpolation records and distinguishes proposed checks from completed development evidence. No scientific campaign, production incident, or job was rerun; no remote environment or queue was changed. GitHub metadata confirmed that the matter-backend code repository is public; the cited paper source repositories remain restricted.
- A fresh-context subagent used canonical paper-style and paper-writing-process skills from research-skills. Its challenge found a real include-syntax bypass in the synthetic checker, an overstatement of repository evidence, and missing validation routes in the portable skill. These were repaired and independently rechecked. The review record includes findings, dispositions, candidate identities, and scope limitations in reviews/adversarial-review-01.md.
- `make check`: twelve tests collected, twelve passed, none skipped. The expanded suite rejects unregistered space/newline/comment-separated and conditional/unbraced includes, and accepts supported whitespace variants for registered inputs. These checks enforce a restricted source grammar, not arbitrary TeX semantics.
- The updated simulation-validation skill passed the skill-creator structural validator using a Python installation with PyYAML. Canonical paper-lint warnings about introduction length, conventional section names, roadmap phrases and figure count were evaluated against the requested concise guide format. They were not treated as scientific defects. The arXiv integrity helper reported zero fatal issues and seven warnings, including its expectation of external bibliography and conventional provenance filenames; this project uses embedded bibliography and paper/generated/results.json. This was not a clean submission audit.
- The final saved main.tex compiled successfully with the built-in document compiler. No separate PDF or rendered visual inspection is claimed. Numerical/citation consistency and whitespace checks passed. Scientific reruns, rendered inspection, and final human submission approval remain outside this revision.
