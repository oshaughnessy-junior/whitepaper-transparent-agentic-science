# Essential skill ports: assessment of agent-skills

This is a recommendation, not a claim that additional skills have been ported or behaviorally validated. The four public skills remain the installed scope. The manuscript change accompanying this assessment is restricted to draft attribution; the paper has not been reorganized around this inventory.

## Scope

Screened the complete on-disk package inventory and repository catalog/provenance documents, then read the core scientific, evidence, citation, writing, reproducibility and continuity workflows and selected supporting contracts, templates and tool interfaces. This is an architectural/content assessment, not an execution or security audit of every script, dependency or live service.

There are **64 top-level skills**, one nested paper-writing stub and one incubator package. The catalog has **63 entries**: it includes the incubator paper-comprehender but omits the on-disk nsf-project-reports and proposal-development packages. Consequently the filesystem, not the catalog alone, was used to screen candidates. These administrative packages do not change the core recommendations.

Source: the access-restricted [agent-skills repository](https://github.com/oshaughnessy-junior/agent-skills). Existing public coverage: result-provenance, simulation-validation, adversarial-science-review, and human-directed-science-writing.

## Highest-priority additions

| Source package or tool | Gap in the current public bundle | Recommended treatment |
|---|---|---|
| **cite-and-verify** | Undefined-key checking does not establish that a reference exists or that it supports its sentence. | Port the two gates: identifier/title identity checking, then semantic claim support with exact locators, evidence notes and dispositions. Include citation_mvf.py, the claim-ledger schema/validator and controlled fixtures. A human assertion records its origin; it is distinct from independent source verification. |
| **audit-bibliography** | Manuscript-level bibliography checking needs structured metadata and identifier-mismatch diagnostics. | Port as the executable bibliography companion to cite-and-verify, retaining its MIT upstream notice and astronomy profile. Keep lookup failure, skipped credentials, metadata drift and an invented reference distinct. Run its regression tests before publishing the port. |
| **science-editing**, with **read-compile-latex** mechanics | The existing writing skill names bounded edits but lacks the full edit contract, semantic freeze and edit ledger. This directly addresses the broad-rewrite failure in this guide. | Port the constrained editing procedure, ledger and canaries; add map/extract/compile helpers as supporting tools. Preserve an accepted title, abstract, argument and voice. A compile/open command is not proof that the rendered document was inspected. Adapt desktop-only opening to the actual client's delivery tools. |
| **autonomous-science** | Four isolated skills do not specify the whole investigation cycle or how a later session resumes a scientific argument. | Port a compact scientific workflow: paper-owned research notes, falsifiable question and acceptance rule, bounded pilot, separate fresh science/code reviews, dispositions, integrated synthesis and resumable checkpoint. Include review contracts and the independence ledger. The source is experimental; a public adaptation needs behavioral validation and retained method attribution. |
| **records-protocol** | Provenance identifies an output but does not decide where measurements, negative results, design decisions and retractions live. | Port a generalized routing table and cleanup procedure. Separate durable evidence from concise code constraints and transient PR discussion. Preserve invariant tests separately from archival paper reproductions. Replace private project-store maps with project-supplied configuration. |
| **paper-writing result toolchain**, especially texresults.py | The public integral example demonstrates a consistency mechanism but is not a reusable logger for arbitrary scientific analyses. | Extend result-provenance with the maintained canonical logger: raw values/intervals, generated macros and JSON records, plus generation/check targets. Inspect the current research-skills implementation rather than copying the deprecated agent-skills snapshot. Require effective configuration, input/code identities and regeneration checks; the inspected legacy interface allows an unknown source and its basic metadata is weaker than the whitepaper's proposed provenance standard. |

**My recommended first batch is the citation pair, bounded editing, and reusable result tooling.** They turn the guide's most concrete promises into usable mechanisms. The research-cycle and records packages follow to make sustained investigations coherent and recoverable.

## Essential practices to fold into existing skills

- **evidence-discipline → simulation-validation and adversarial-science-review.** Preserve the strongest missing details: benchmark proxies can answer the wrong question; an unswept dimension remains a limitation; a tuning input may not identify the requested decision; fixtures must distinguish alternatives; configuration must change the computation; stale guidance must be removed across user-facing surfaces. Much of mutation testing, test-count checking, seed variation and actual-entry-point validation is already present. Avoid duplicating the whole skill or importing private numerical anecdotes. A mature-code disagreement still merits investigation; checking the harness first must not become an exemption from scrutiny.
- **project-sandboxing → simulation-validation.** A locked project environment and imported-module identity are essential to reproducibility. Keep the invariant, support the project's actual environment manager, and remove assumptions that Pixi or a particular machine layout is universal.
- **verification-before-completion → workflow closeout.** Require receipts for what ran, compiled, rendered, committed and was delivered. Missing checks stay explicit. A separate generic checklist adds little when this is already built into the owning workflow.
- **task-handoff / long-running-task-management / session-teams → autonomous-science.** Preserve bounded ownership, checkpoints, job identity, next action, and checks against duplicate launches. Do not make OpenClaw state-manager scripts, named session types, host aliases, quotas or private coordination services prerequisites for the public guide.
- **scientific-writing → human-directed-science-writing.** Port the writing packet, logical-claims audit and distinction among observation, inference and implication as supporting templates. Keep structure guidance flexible and respect the human outline. Avoid a second competing writing umbrella.

## Useful, conditional extensions

- **computer-algebra:** valuable for consequential derivations, signs, factors, limits and generated kernels; include assumptions and a reproducible check. Generalize hard-coded interpreter paths and stale licensing assumptions. It is essential when a claim depends on fragile algebra, not a mandatory invocation for every paper.
- **research-corpus:** the portable evidence-bundle format is useful for source identity, locators, freshness, omissions and checksums. A live corpus/librarian service is optional; a bounded static packet and primary-source verification can satisfy the contract.
- **ads-search / arxiv-search / bibtex-manager:** useful discovery/import adapters; bundle only what the citation tools need. Discovery, bibliographic identity and scientific support remain separate jobs. Use environment-held credentials and report missing access honestly.
- **condor-ops / log-analyzer / log-observability:** optional production adapters. Their domain is scheduler and operational diagnosis, not a universal scientific standard.
- **deep-research / paper-summarizer:** optional discovery and synthesis aids; their output still needs source-support checks. Do not require a swarm, large fan-out, a specific citation style or arbitrary cycles per theme for an ordinary bounded writing task.

## Port boundaries

Adapt selected procedures and their direct support files; do not import the entire repository or private runtime records. Preserve third-party licenses and attribution. In particular, audit-bibliography has a retained MIT upstream license and autonomous-science records attributed method adaptations. Strip host paths, private store maps, credentials and unpublished examples. Validate schemas, negative controls and real behavior as well as SKILL.md structure.

The paper-writing snapshot is explicitly deprecated in favor of research-skills. Do not propagate its unverified arXiv penalty assertions or rigid article skeleton as a public scientific requirement. Current venue policy belongs in a separately verified policy record. Existing human instructions govern this guide's structure.

## Complete top-level screening inventory

The following records a disposition for every top-level package, rather than only the recommended subset. “Exclude” means outside this scientific-method bundle, not that the skill has no value in its original runtime.

| Package | Disposition |
|---|---|
| a2a-communication | Exclude from the core scientific-method bundle |
| academic-deep-research-pro | Conditional support; not an additional core requirement |
| academic-literature-search | Conditional support; not an additional core requirement |
| accli | Exclude from the core scientific-method bundle |
| ads-search | Conditional support; not an additional core requirement |
| ag | Exclude from the core scientific-method bundle |
| agent-self-recovery | Exclude from the core scientific-method bundle |
| arxiv-search | Conditional support; not an additional core requirement |
| audit-bibliography | Port a focused package |
| autonomous-science | Port a focused package |
| bibtex-manager | Conditional support; not an additional core requirement |
| blocker-identification | Exclude from the core scientific-method bundle |
| caffiene-persistence | Exclude from the core scientific-method bundle |
| caldav-calendar | Exclude from the core scientific-method bundle |
| cite-and-verify | Port a focused package |
| claude-code | Exclude from the core scientific-method bundle |
| computer-algebra | Conditional support; not an additional core requirement |
| condor-ops | Conditional support; not an additional core requirement |
| context-pruning | Conditional support; not an additional core requirement |
| continuity | Exclude from the core scientific-method bundle |
| dcc-use | Exclude from the core scientific-method bundle |
| deep-research | Conditional support; not an additional core requirement |
| duo-gated-access | Exclude from the core scientific-method bundle |
| evidence-discipline | Integrate/adapt into existing skills or tooling |
| executing-plans | Conditional support; not an additional core requirement |
| file-integrity-manager | Conditional support; not an additional core requirement |
| harness-testing | Conditional support; not an additional core requirement |
| health-maintenance | Exclude from the core scientific-method bundle |
| heartbeat-governor | Exclude from the core scientific-method bundle |
| installed-skill-auditor | Exclude from the core scientific-method bundle |
| large-file-interceptor | Conditional support; not an additional core requirement |
| llo-orchestrator | Exclude from the core scientific-method bundle |
| log-analyzer | Conditional support; not an additional core requirement |
| log-observability | Conditional support; not an additional core requirement |
| long-running-task-management | Integrate/adapt into existing skills or tooling |
| loop-circuit-breaker | Exclude from the core scientific-method bundle |
| memory-graph-builder | Exclude from the core scientific-method bundle |
| memory-reflect | Exclude from the core scientific-method bundle |
| mission-control | Exclude from the core scientific-method bundle |
| nsf-project-reports | Exclude from the core scientific-method bundle |
| pages-deploy-watchdog | Exclude from the core scientific-method bundle |
| paper-summarizer | Conditional support; not an additional core requirement |
| paper-writing | Integrate/adapt into existing skills or tooling |
| paper-writing-process | Integrate/adapt into existing skills or tooling |
| project-sandboxing | Integrate/adapt into existing skills or tooling |
| proposal-development | Exclude from the core scientific-method bundle |
| ralph-loop-orchestrator | Exclude from the core scientific-method bundle |
| read-compile-latex | Integrate/adapt into existing skills or tooling |
| records-protocol | Port a focused package |
| report-surface | Exclude from the core scientific-method bundle |
| research-corpus | Conditional support; not an additional core requirement |
| sandbox-provisioner | Conditional support; not an additional core requirement |
| science-editing | Port a focused package |
| scientific-writing | Integrate/adapt into existing skills or tooling |
| secure-local-documents | Conditional support; not an additional core requirement |
| self-improving-agent | Conditional support; not an additional core requirement |
| session-teams | Integrate/adapt into existing skills or tooling |
| skill-loadout-manager | Exclude from the core scientific-method bundle |
| state-checkpointing | Exclude from the core scientific-method bundle |
| state-system-governor | Exclude from the core scientific-method bundle |
| task-handoff | Integrate/adapt into existing skills or tooling |
| verification-before-completion | Integrate/adapt into existing skills or tooling |
| web_search | Exclude from the core scientific-method bundle |
| writing-plans | Conditional support; not an additional core requirement |

The nested paper-writing stub is an alias/distribution aid, not another procedure. The incubator paper-comprehender is unfinished and not a core port recommendation. No new skill packages were copied or installed during this assessment.
