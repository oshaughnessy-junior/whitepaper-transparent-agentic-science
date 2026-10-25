# Contrast cases: intentionally limited human involvement

The commissioning human explicitly identifies these aiXiv postings as exercises of independent agentic capability, operated without the close human drafting guardrails advocated in the whitepaper. Humans supplied high-level direction. This is design metadata supplied by the commissioning human; it is not inferred from writing quality or from AI authorship labels. It is retained as human-asserted in aixiv-contrast-claims.json.

This contrast does not mean no tools, provenance, prompts or agent-side procedures were used. Public source repositories contain their own writing/evidence packets and internal agent review; the compute-islands paper also uses logged numerical results. Those practices are compatible with the deliberate absence of close human control of manuscript structure and section edits. The public phrase “author-directed AI work” identifies the producing/reviewing team; it does not establish that a human closely edited the manuscript.

## Inspected versions

| Posting | Version inspected | Claim-bearing material read | Evidence boundary |
|---|---|---|---|
| [MCRP verification lifecycle](https://aixiv.science/pdf/aixiv.260925.000008v1.5.pdf) | v1.5 | Abstract, evidence withdrawal, proposed evaluation and lifecycle limitations | A policy proposal with synthetic tests, not demonstrated effectiveness |
| [Small contracts, measurable limits](https://aixiv.science/pdf/aixiv.260925.000007v1.4.pdf) | v1.4 | Abstract, modeling boundary, audience/prior-work scope and conditional results | Mathematical/toy-model evidence, not calibration of reviewer behavior |
| [Local scientific investigators](https://aixiv.science/pdf/aixiv.260925.000009v1.0.pdf) | v1.0 | Motivation, local/coordinator roles, Sections 4.5–4.6, conclusion and data/code statement | Executed local experiment loop and subsequent claim correction; wider architecture remains proposed |

The public posting pages were checked directly; their PDF links supplied the pinned files. aixiv-postings.json records the public PDF hashes. Source-repository READMEs were also inspected through GitHub: [mcrp-protocol-paper](https://github.com/oshaughnessy-junior/mcrp-protocol-paper) and [trust-and-review-papers](https://github.com/oshaughnessy-junior/trust-and-review-papers). Some README upload-status statements lag the posting pages; the appendix cites the actual downloaded posted versions. Later source work is not silently assigned to an earlier PDF. The compute-islands PDF describes its implementation/transcripts as private at that posting; current repository visibility was not independently established here.

## What the comparison can establish

The cases expose distinct capabilities: constructing a protocol and its checks; conditional mathematical modeling and counterexamples; executing an adaptive experiment loop; and correcting an unsupported interpretation. They also provide material for judging how the manuscript separates tested results from a larger proposed program and how it prioritizes the supported contribution.

The contrast is qualitative. No matched prompt/model/budget experiment or human-involvement ablation was conducted for the whitepaper. These are reviewed posted versions, not necessarily pristine first drafts. No underlying scientific jobs or source-repository tests were rerun here. The resident Gemma investigator in the compute-islands pilot is a smaller-model exception to the whitepaper's usual frontier baseline; Codex drafted/operated/reviewed a different part of that workflow. A failed local interpretation is not attributed automatically to the stronger coordinator.

Only public sources and sanitized design metadata enter this case record. Private transcripts, host paths and unpublished work are excluded. The main paper's framing and abstract are preserved; the change is one appendix plus its bibliography entries, shown in ../docs/reviews/aixiv-appendix.patch.
