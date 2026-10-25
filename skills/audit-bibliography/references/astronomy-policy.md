# Astronomy bibliography policy

## Authority order

1. Use an explicit ADS bibcode through NASA ADS when `ADS_API_TOKEN` is available.
2. Resolve an arXiv identifier through arXiv.
3. Resolve a DOI through Crossref, then DataCite for non-Crossref registrants.
4. Use exact-title search only as an advisory fallback.

ADS, arXiv, and publishers may legitimately disagree on preprint versus publication year, title punctuation, and collaboration author lists. Treat those as metadata review unless the identifier directly resolves to a different work.

## Formatting

Whole-title protection is normal in ADS-exported BibTeX. The astronomy profile does not flag it. Preserve journal macros and project-specific citation keys unless the owning manuscript requests normalization.

## Collaboration and non-article records

Do not infer fabrication from abbreviated collaboration authorship, software repositories, data releases, technical reports, or web resources. Mark their type accurately and verify their canonical URL or DOI. A registry miss for grey literature is inconclusive.

## Publication gate

Fail automatically for:

- a cited work that remains unfindable after authoritative and manual checks;
- a DOI, arXiv ID, or ADS bibcode that directly identifies no work or a different work;
- an author credited in the bibliography who is absent from the identifier-pinned record.

Warn without failing for metadata drift and style. Verify claim support in a separate semantic review.
