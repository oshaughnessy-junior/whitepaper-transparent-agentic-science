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
