# Independent adversarial review of the skill ports

Reviewer: separate Codex subagent assigned gpt-6.1-sol, high reasoning effort. This was a bounded follow-up by the reviewer used earlier for the guide, with a fresh port task; it was not a second newly blinded reviewer. The reviewer did not edit the candidate. It used synthetic temporary inputs, mocked transport and synthetic credentials; no real credentials, live API requests, user cache inspection or scientific campaigns were involved.

Final verdict: **the reviewed ports are acceptable after repairs; no remaining actionable code or privacy defect was found in the exercised paths.** The reviewer did not certify the subsequently completed port-record prose.

## Findings and dispositions

| Severity | Finding | Repair and independent recheck |
|---|---|---|
| High | A substring check attached a Semantic Scholar credential to a Crossref query containing the provider's name. | Exact HTTPS-host/port/userinfo checks now govern credentials; protected redirects are refused in both metadata packages. Synthetic wrong-destination and redirect probes passed after repair. |
| Medium | Empty DOI metadata, mismatched arXiv records and absent expected-title metadata could verify. ADS query punctuation was also incorrectly interpolated. | Require returned identity and usable metadata, check requested versions/titles, encode ADS parameters. Independent positive and negative DOI/arXiv/ADS cases passed. |
| Medium | Legacy cached success could bypass stricter validation. | Namespace cache keys by verifier schema and reject missing/old schema stamps. Temporary legacy/current cache pairs were independently checked. |
| Medium | A result's arbitrary display could contradict its raw value; a Lambda key could overwrite a scientific math command. | Removed display overrides; derive rendering from raw values and rounding. Namespace generated keys. Reviewer checked failure/success pairs. Author also compiled a synthetic Lambda example successfully. |
| Medium | The ledger accepted an absent/nonstring human verifier. | Require a nonblank named verifier for human-asserted claims; source verification remains a separate disposition. Independent malformed/named pairs passed. |
| Low | Citation --summary raised a missing-key exception, and ordinary whitespace/comment result syntax escaped checks. | Repaired summary output and result-use syntax handling; actual CLI and positive/negative syntax regressions pass. |

All findings were retained and rechecked; none remains open within this scope.

## Evidence and limits

The reviewer independently ran the root suite (**34 passed, none skipped**) and bibliography suite (**64 passed, none skipped**), separate synthetic probes and git diff --check. It found no private host paths, real credentials, runtime state, raw memories or unpublished numerical results in the inspected port files. This is not a guarantee about arbitrary future generated reports or manifests. Review those before publication.

The reviewer confirmed retained MIT upstream attribution, bounded editing behavior, and the research workflow's resource and authorization boundaries. It did not independently establish source ownership beyond the user's authorization and retained attribution. Live service compatibility, complete parser coverage, scientific correctness and production validation remain outside the verdict.

Reviewed executable SHA-256 snapshots, identifying these public adaptations:

- citation_mvf.py: `1bd8fee3dbc76843a14705b23d9d17c361e85fa33678cf5fd91c9bb8a4fce5ba`
- validate_claim_ledger.py: `a814dea9a9843f938e80d4081feedae13e1b8a53892cf23384ded89ea3d82701`
- texresults.py: `43a6bfe7ad6a9296deee886a1dcad8caaf4912321ac836212ac4e690878c235e`
- bibmeta.py: `473f93ffe6c4b284c06fc787edc1f8a21ae41a3f1c891b3df1b836a85e9bcded`
