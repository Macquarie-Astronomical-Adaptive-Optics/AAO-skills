---
name: paper-downloading
description: Download, organize, and document research papers for AAO workflows using lawful access paths. Use when finding paper metadata, recording DOI and source provenance, saving PDFs into a project convention, or creating paper-download scripts and checks without bypassing access controls.
---

# Paper Downloading

## Workflow

- Use lawful access paths only. Do not bypass paywalls, license restrictions, authentication, or publisher controls.
- Capture bibliographic provenance: title, authors, year, DOI, arXiv identifier if present, landing page URL, download URL, and access date.
- Prefer stable identifiers and publisher or repository landing pages over raw PDF URLs when recording sources.
- Keep file naming deterministic and readable. Follow any project-specific convention supplied by the user.
- Use scripts in `scripts/` for repeatable metadata checks, download manifests, or validation once those scripts are added.
- Keep sensitive project reading lists or partner-private literature notes out of this broadly shareable repository.

## Two-Pass Reading-List Workflow

Use this pattern when the first pass identifies papers from titles, abstracts,
publisher snippets, or other public metadata, and the second pass tries to make
the papers practically readable.

1. Discovery pass:
   - Record who or what produced the candidate list, the date, the ranking
     criterion, and the evidence used. For example, in the 2026-05-05 RFS LWIR
     camera work, GPT-5.5 Pro first found candidate papers from titles,
     abstracts, publisher pages, and public metadata, ranked by direct
     usefulness to a low-altitude drone-mounted LWIR payload rather than by
     citation count.
   - Preserve uncertainty separately from bibliographic facts. If a SPIE,
     Optica, IEEE, or other publisher page was located but not opened or not
     downloaded, say exactly that.
2. Alternate-access pass:
   - For every paper, search the exact title and DOI against arXiv, SSRN, HAL,
     Zenodo, OSF, PubMed Central, institutional repositories, government
     repositories, author web pages, OpenAlex/Unpaywall-style OA metadata,
     Crossref, Semantic Scholar, and ordinary web search.
   - Record exact-paper access separately from related versions. Later expanded
     papers, conference precursors, datasets, code packages, and review articles
     can be useful, but they are not substitutes for the exact paper.
   - Mark ResearchGate, Academia.edu, and similar social-repository pages as
     access leads with license/copyright caveats unless the page clearly states
     a lawful open license.
   - Explicitly record `no alternate full text found in this pass` when a search
     only finds metadata, abstracts, citations, or the primary publisher page.
3. Manifest fields:
   - `status`: to-read, downloaded, metadata-only, no-alternate-found, or
     related-version-only.
   - `primary_record`: DOI or publisher landing page.
   - `alternate_records`: repository, preprint, author-page, government, PMC, or
     dataset/code URLs.
   - `full_text_available`: yes/no/unclear.
   - `license_or_caveat`: CC license, repository terms, ResearchGate caveat, or
     unknown.
   - `access_date`: date the access lead was checked.
   - `notes`: version mismatch, page-range discrepancy, exact/related-version
     distinction, or missing metadata.

## Output Expectations

- Report what was downloaded, where it was saved, and which source was used.
- Flag missing metadata, uncertain versions, license restrictions, or access failures.
- Avoid presenting a PDF as authoritative when only an abstract or metadata page was available.
