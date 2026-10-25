# Behavioral checks

These are synthetic editing cases, not findings about an actual paper.

- Request: shorten “Within the tested regime, the model may improve recovery.” An edit to “The model improves recovery” fails: it removes the domain and strengthens the claim.
- Request: clarify a paragraph containing a protected equation and citation. An edit that changes a symbol, inequality or the citation's attached claim fails even if compilation succeeds.
- Request: tighten a section; the accepted title and abstract are supplied as context. Replacing either fails the edit contract. Return a bounded diff and propose any broader change separately.
- Conflicting evidence: a supplied table does not support a sentence. Do not disguise a claim repair as line editing. Flag the scientific decision outside the clean revision.
