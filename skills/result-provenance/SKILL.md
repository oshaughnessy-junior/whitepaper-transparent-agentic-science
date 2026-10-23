---
name: result-provenance
description: Generate and verify scientific result macros, tables, and figure annotations from a shared result record. Use for computed manuscript numbers and companion-paper consistency.
---

# Result Provenance

Log results at the point of computation. Store raw value, units, uncertainty definition, producing command/code revision, input/configuration hashes, seed/run identity, and scientific scope. Never substitute a plausible value for pending evidence.

Use stable semantic keys. Generate every presentation of the same quantity from that key with explicit rounding rules. Share the record across companion papers; do not synchronize copied macros by hand. Generate table cells and figure annotations from the same record.

Distinguish current, stale, intentionally frozen historical, curated input, and missing-producer records. A frozen result retains its original sample/domain with a visible explanation. A curated constant requires a source; it is not a measured result.

Regenerate into a clean temporary directory, compare all generated artifacts, check every result use, and trace provenance back to completed outputs. Exercise a stale/corrupt artifact to show the check fails. Document parser coverage: defined macro names alone establish neither freshness nor correctness. See ../../docs/workflow.md and the runnable ../../tools/evidence.py demonstration.

Key caches from the actual dependency closure, including calibration and environment-sensitive inputs. Reject products missing required identity stamps; do not infer freshness from timestamps. Key data at construction and assert an identifying physical invariant before caching. Record optimizer initialization, phases, restart schedule, checkpoints and the rule choosing the reported iterate. Sweep every caller and downstream summary after a convention change. See ../../docs/cardassia-lessons.md.
