---
name: simulation-validation
description: Validate scientific simulation and inference results using independent routes, uncertainty, convergence, and negative controls. Use before promoting computational outputs to claims.
---

# Simulation Validation

Define domain, observable, acceptance threshold and failure cases before tuning. Run a small pilot through the production entry point before scaling. Verify important configuration changes affect the intended output.

Compare an analytic or limiting answer where possible, structurally different implementations, grid/timestep refinement, and multiple independent seeds. Separate stochastic uncertainty, numerical approximation, and model discrepancy. Test boundaries, units, normalization, singular or invalid inputs, and observable-space predictions as relevant.

Record reference lineage and whether cases were used to fit, select, or repair the candidate. Shared code and assumptions limit independence. After tuning on a holdout, reserve new confirmation cases or keep the result provisional.

Use a deliberate corruption in an isolated copy to demonstrate that the gate detects a relevant defect. Record actual collected/passed/skipped test counts and raw failures. Preserve disagreement until explained; inspect the harness before declaring a mature reference wrong.

Save exact code/input/configuration/environment identities, commands, seeds, output hashes and job status. A live job is not evidence. Integrate a scoped scientific conclusion into durable notes. See ../../docs/workflow.md.

For inference inputs, distinguish posterior from likelihood, inspect prior division and coordinate measure, and retain needed covariance. At physical boundaries, validate density-estimation behavior. Compare computational costs at matched accuracy. Separate library-size limitations from integration noise before proposing an estimator repair. Read effective settings from the output itself and compare them with the intended configuration. See ../../docs/cardassia-lessons.md.
