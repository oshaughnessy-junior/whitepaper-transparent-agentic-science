# Star–black-hole dynamics: main-paper example

This case concerns **only the main dynamics paper** in the [encounter-recipes repository](https://github.com/oshaughnessy-junior/starbh_paper_A-encounter-recipes), a working draft whose repository access was confirmed restricted on 2026-10-25. The user selected this paper as an additional example. Local project memory, the manuscript, implementation and recorded reviews were inspected read-only, together with cardassia's archived run documentation. The scientific source repository was not edited.

## Concrete lessons

| Observation in the inspected records | Practice supported |
|---|---|
| A normalization concern required tracing incoming flux, proposal density, inclusion probability, the all-proposal denominator and conditional sampling into the final population rate. The apparent isolated prefactor discrepancy canceled in the complete calculation. | Review the whole estimator before changing a local factor. Check absolute normalization with analytic limits as well as agreement between implementations. A correct implementation can need a clearer derivation rather than a rescaling. |
| Seeded output fixtures failed after a dependency change. Matched-environment old/new code agreed. Fixed-interpreter dependency comparisons traced an early difference to floating-point evaluation of uniform sampling despite matching random bits. Neither comparison reconstructed the fixture's original platform exactly. | Preserve environment and fixture-generation provenance. Distinguish bitwise reproduction, numerical tolerance and scientific invariants. Do not replace expected hashes solely because the current output is stable or two code revisions agree. |
| The remote run archive contained completed-run metadata, code identities, kernel outputs and convergence records. The kernel and convergence record, and all inspected producing code files, matched their recorded hashes. The corresponding checkout note still described an early scaffold. | Resolve the producing run and its imported/archived code rather than treating a checkout name or memory summary as execution evidence. Memory provides leads; artifacts establish which run is being discussed. |
| Multiple generated result bundles share a manuscript namespace. The shared build helper rejects the same key with conflicting rendered values. | Allocate semantic namespaces and reject conflicting definitions before TeX input order can choose a value. Identical display text alone does not establish identical scientific meaning; units, scope and producer still need review. |

The main dynamics manuscript describes the estimator and uses generated result bundles. Its recorded kernel review examined the implementation, limiting cases and archived convergence evidence. Its development feedback distinguishes unresolved fixture provenance from a demonstrated change between source revisions. These are complementary forms of review rather than a single test badge.

## Skills and reproduction route

- **result-provenance:** preserve the producing configuration, dependency identities, raw outputs and stable result keys; check merged result bundles for conflicting definitions.
- **simulation-validation:** use analytic limits, matched-environment previous-code comparisons, solver controls and representative production records. Specify whether a comparison asks for bitwise identity or agreement at a scientific tolerance.
- **adversarial-science-review:** challenge the mathematical measure, selection/inclusion weights and end-to-end operator route; require evidence before accepting a proposed repair.
- **human-directed-science-writing:** resolve normalization definitions and physical scope before polishing an explanation; keep the main paper's argument distinct from chronological project notes.

A complete rerun requires repository access, its identified inputs and producing environment. This inspection verified selected recorded identities and read the diagnosis; it did not rerun the encounter grids or change regression baselines. No unpublished rates, scientific parameter estimates, private run paths, memory excerpts or source revision identifiers are released here. Detailed reconstruction locators remain in a separate local restricted audit.
