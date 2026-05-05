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

## Output Expectations

- Report what was downloaded, where it was saved, and which source was used.
- Flag missing metadata, uncertain versions, license restrictions, or access failures.
- Avoid presenting a PDF as authoritative when only an abstract or metadata page was available.
