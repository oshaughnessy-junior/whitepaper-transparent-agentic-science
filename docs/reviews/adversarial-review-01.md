# Adversarial review of the human-facing guide

This is an author-recorded summary of the independent review and its dispositions. It covers the guide and synthetic checker, not certification of the cited scientific campaigns.

## Reviewer and exposure

A separate Codex subagent, assigned `gpt-6.1-sol` with high reasoning effort, received a fresh context rather than the authoring conversation. It used the canonical `paper-style` and `paper-writing-process` skills from the access-restricted research-skills repository. Human instructions to make this guide concise and accessible with boldface and lists governed format. The reviewer did not implement repairs. Subsequent passes reused that reviewer to inspect dispositions; they were not additional independent first-pass reviews.

Initial manuscript SHA-256: `88abf18e6615d3ae5f7cfcd666dcc9999ab07fb724fb00ecacf5f8d3599df130`.

Repaired candidate independently checked: `0b14196ce56a63610471240a0e02455634eb8a33c9d5c4f8f61e56b8b14876e4`.

Final manuscript SHA-256: `1fff4942453475cc8439a82c996924e019a077154b701f761d328030066829fe`.

These hashes identify this public manuscript, not restricted source repositories.

## Findings and dispositions

| Severity | Finding | Repair and recheck |
|---|---|---|
| Medium | The checker recognized `\\input{...}` but could miss an unregistered file introduced with `\\input {...}`, allowing an unchecked numerical claim. | Count include commands separately from supported braced arguments; normalize comments; reject unsupported/conditional inclusion routes. Added negative whitespace/comment/unbraced/conditional cases and positive registered-whitespace cases. Reviewer independently demonstrated rejection of the original counterexample and variants. |
| Medium | The abstract described required repository evidence as if already completed for all examples. | Changed to a prescriptive standard and added an explicit evidence boundary: only the synthetic example was executed for this guide. Reviewer confirmed the distinction. |
| Low | The simulation-validation skill omitted explicit paper-example, previous-code, literature and production-route validation. | Added all four routes and an archived receipt with identities, tolerances, baseline comparison and missing coverage. Reviewer confirmed. |
| Low, follow-up | The matter-backend root link did not directly expose the evidence supporting the solver/interpolation claims. | Added dated public logs and the validation-deepening plan to the case inventory, distinguishing completed comparisons from proposals and evolving default-branch records. Final reviewer closed the finding. |

## Verification and final verdict

During the preceding pass, the reviewer independently ran `make check`: **12 tests passed, none skipped**, and exercised syntax counterexamples in temporary copies. The author reran the same suite after final edits and compiled the saved manuscript with the built-in LaTeX compiler.

Final reviewer verdict: **“accepted. No remaining actionable findings in this bounded review.”** The final pass verified the manuscript hash above, read the changed manuscript and inventory, independently confirmed NuclearMatter-Backend's public GitHub visibility, and checked that the appendix accurately reports the demonstrated defect and limited guarantee. It did not repeat the earlier test run. All initial findings and the follow-up navigation finding were closed.

## Limits

The reviewer did not rerun the population or RIFT/matter-backend scientific campaigns, independently verify remote host histories, inspect the rendered PDF, or authorize submission. Host-memory lessons remain attributed inspected records, not independently reproduced incidents. Acceptance is for a human-facing working guide within this scope. It is not a performance benchmark or a universal TeX guarantee. Full scientific review and human approval remain necessary before submission.
