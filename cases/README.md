# Main-paper examples and evidence status

Only each repository's main paper is in scope.

| Case | Source | Established here | Still pending |
|---|---|---|---|
| Tooling | [agent-skills](https://github.com/oshaughnessy-junior/agent-skills) (restricted access) | Procedure inspection and public synthetic consistency example | Independent validation of the complete protocol |
| Synthetic universes | [popsynth_hyperpipe_paper](https://github.com/oshaughnessy-junior/popsynth_hyperpipe_paper) (restricted access); [main preprint](https://arxiv.org/abs/2609.05996) | Public text distinguishes a hypothesis from a numerically supported evidence comparison | Full independent numerical rerun |
| Hierarchical modeling | [gwk-hierarchical-initial](https://github.com/oshaughnessy-junior/gwk-hierarchical-initial) (restricted access); [main preprint](https://arxiv.org/abs/2609.06728) | Selected public passages document an input-representation retraction, detected-tail test, and prior-bound limitation | Full independent numerical rerun |

These are related scientific applications, not independent samples for measuring agent performance. Public textual grounding is distinct from executing the underlying analysis. The public source map is in PROVENANCE.md; detailed private-source audit records remain local. A complete reproduction packet needs identified inputs, producer/configuration, commands, comparisons and final reviewed outcomes.

## RIFT review sequence and third-generation study

The user additionally requested RIFT development as an example. These links currently require repository access. PR metadata and descriptions were read directly on 2026-10-23; the listed PRs were merged. No underlying numerical campaign was rerun for this guide.

| Review record | Concrete diagnosis | What the recorded check establishes |
|---|---|---|
| [Per-sample offset repair, PR 234](https://github.com/oshaughnessy-junior/research-projects-RIT/pull/234) | A batch-wide log-likelihood offset underflows otherwise valid rows; broadcasting can conceal an incorrect repair | Actual likelihood-path regression, square-array case, and mutations of the offset/shape repair |
| [Hermite quadrature, PR 266](https://github.com/oshaughnessy-junior/research-projects-RIT/pull/266) | Valid non-finite rows rejected; endpoint claim false; fixture vacuous; CLI and dispatch did not exercise the new rule | Analytic and boundary checks, discriminating fixtures, subprocess selection checks, and mutation tests |
| [Backend-consistent quadrature, PR 459](https://github.com/oshaughnessy-junior/research-projects-RIT/pull/459) | The same rule name selected different CPU/GPU quadratures | Backend comparisons and mutations; the PR explicitly reports no end-to-end known-answer parameter-estimation run |

The associated main scientific study is [Scaling RIFT 1](https://arxiv.org/abs/2609.37393), already posted on arXiv. Its [source repository](https://github.com/oshaughnessy-junior/RIFT_roboto_paper) currently requires access. The PR sequence includes work later than that posted version: do not imply that every repair or subsequent result is contained in the preprint. Forthcoming studies and future revisions remain distinct from completed review evidence. No unverified titles or publication details are assigned to future work.

## NuclearMatter-Backend and lessons from the run hosts

The [NuclearMatter-Backend code repository](https://github.com/oshaughnessy-junior/NuclearMatter-Backend) is **public**, as confirmed through GitHub metadata during this revision. Its paper repositories and host project memories are separate, restricted sources. The code example is cited here under its package name `nmbackend`.

**Follow the dated evidence, not just the README:**

- [Adaptive-solver validation log](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/docs/devlog/2026-06-02b-validation-adaptive-solver.md): an independently formulated radius-domain solve exposed under-resolution in the earlier enthalpy-domain implementation and motivated an adaptive default. The log distinguishes the in-process reference from external corroboration still owed at that point.
- [Consistent-interpolation log](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/docs/devlog/2026-06-02f-consistent-interpolation.md): subsequent comparisons separate surface conventions and thermodynamic interpolation from integration error; derivative accuracy requires its own tolerance study. This later record is more specific than older README status text.
- [Validation-deepening plan](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/docs/validation-deepening.md): distinguishes completed comparisons from proposed broader external-solver, physics-model and paper-scale checks. Its plans are not reported as completed validation here.

These are records of development, not reruns performed for the white paper. Current branch/release validation still requires its own receipt; the linked default-branch documents can evolve.

**Additional recorded lessons inspected read-only:**

| Host | Lesson incorporated | Evidence boundary |
|---|---|---|
| CIT | Repeated JAX compilation can fail under production resource limits; derivative and residual checks need independent value-level paths | Project-memory reports inspected; no incident or scientific campaign rerun |
| cardassia | Long jobs need an explicit follow-on execution path and bounded worker resources; a watcher notice alone does not complete the next step | Project-memory and validation-plan inspection; no job launch or current job-status assertion |
| sporc | Editable installs can import a different checkout; shared dependency pins and branches can move during a session | Project-memory reports inspected through the existing connection; no environment or queue mutation |

The resulting prescription is to record imported-module identity inside the run, validate the delivered revision in its real environment, preserve immutable input/output identities, and separate completed evidence from plans. Raw memory, private file paths, session identifiers, revision hashes and unpublished numerical results are excluded from this public inventory.

## Deliberately low-human-involvement contrast

The [aiXiv contrast record](aixiv-contrast.md) covers the separate, intentionally minimally supervised capability exercises requested for the appendix. Its public sources, pinned versions, human-asserted experiment conditions and limits are recorded separately from the closely guided main-paper cases. It is not a controlled comparison or certification of the experiments.
