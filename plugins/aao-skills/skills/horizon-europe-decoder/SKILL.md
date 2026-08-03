---
name: horizon-europe-decoder
description: Decode Horizon Europe grants for AAO and approved collaborators. Use when explaining the scheme, finding or shortlisting calls and topics, checking eligibility or participation routes, interpreting topic conditions and application templates, comparing strategic fit to organisation or company capabilities, or preparing an evidence-backed opportunity brief.
---

# Horizon Europe Decoder

Turn an opaque Horizon Europe search or topic page into an auditable decision brief. Treat this as grant-opportunity analysis, not procurement advice: the Funding & Tenders Portal contains both grants and tenders, and the two routes have different rules.

## Safety and circulation boundary

- Confirm that the work is safe for broad AAO or approved-collaborator circulation.
- Keep unpublished strategy, partner-private information, named-company assessments, proposal drafts, sensitive technical detail, export-control concerns, security classifications, and internal go/no-go decisions out of this repository. Use them only as task inputs unless the user explicitly asks to save them in an approved location.
- Move controlled, security-sensitive, Defence-adjacent, commercially sensitive, or clearance-dependent work to the restricted repository workflow.
- Prefer anonymised company IDs for exploratory portfolio matching. Do not persist a supplied company list or inferred company weaknesses without explicit permission.

## Choose the mode

Use the smallest mode that answers the request:

1. `Scheme explainer`: explain Horizon Europe concepts or the application process.
2. `Opportunity scan`: find and shortlist current topics for a capability, domain, date window, or organisation.
3. `Topic decoder`: turn one topic into a plain-language brief with hard gates and open questions.
4. `Strategic fit`: compare one or more topics with supplied organisation or company profiles.
5. `Application map`: map a confirmed target topic to the current application form, budget workbook, evidence needs, and proposal work plan.

Do not start proposal drafting merely because a topic sounds relevant. First confirm the exact topic, participation route, deadline, hard eligibility gates, expected outcomes, scope fit, and the user's intended role.

## Minimum inputs

Use available context before asking questions. Collect only what the selected mode needs:

- the user's question, search terms, or exact topic identifier
- the organisation's country and intended role: coordinator, beneficiary, affiliated entity, associated partner, subcontractor, or unknown
- the relevant capabilities, evidence, starting TRL, desired outcome, and date horizon
- any known partners, exclusions, funding constraints, or confidentiality classification

If the user asks only for a general explanation, do not require an organisation profile. If a missing fact could reverse eligibility or a go/no-go recommendation, mark it as a hard unknown rather than guessing.

## Source-first workflow

1. Open `references/source-hierarchy.md` and follow its source order.
2. Establish a dated source snapshot. Record each source's title, URL or file path, version/publication date, access date, and relevant page or section.
3. For current status, opening date, deadline, budget, topic documents, and submission conditions, inspect the live official Funding & Tenders Portal topic page. A saved work programme is not proof that a topic is still open or unchanged.
4. Read the current topic text together with the current General Annexes, Programme Guide, participating-countries guidance, and topic-specific conditions. Topic-specific conditions override generic summaries.
5. Use official National Contact Point guidance or a relevant EU agency page as clarification, not as a substitute for the topic and governing documents.
6. Use third-party summaries only for discovery or context. Never use them as the sole evidence for eligibility, deadline, funding, consortium, security, or submission claims.
7. Keep three evidence states distinct:
   - `confirmed`: directly supported by a current official source
   - `inferred`: reasoned from confirmed facts, with the inference stated
   - `unknown`: not resolved by the inspected sources

For optional machine-readable discovery and the dated assessment of existing hosted MCP services, see `references/existing-integrations-2026-08-03.md`. A third-party MCP result is a lead, not authority for eligibility, status, deadlines, or submission requirements.

When a local work-programme PDF is available, use `scripts/extract_work_programme.py` to create a candidate index or inspect a topic block. The script is a discovery aid; it does not establish live status or final eligibility.

```bash
python3 scripts/extract_work_programme.py /path/to/work-programme.pdf \
  --topic-prefix HORIZON-CL4-2026-SPACE \
  --format markdown \
  --output /path/to/topic-index.md
```

Use `--topic HORIZON-...` for one exact topic and repeat `--query TERM` for AND-matched terms. Install Poppler if `--check-dependencies` reports that `pdftotext` is missing.

Use `--diagnose --format json` when the input document is uncertain. The diagnostic distinguishes a main Horizon work programme from the General Annexes, the EIC work programme, Digital Europe material, and an EU procurement dossier. Route non-topic documents to their own rules instead of treating a zero-topic result as evidence that they contain no opportunities. See `references/field-test-2026-08-03.md` for the evaluated corpus, observed outputs, and current parser boundary.

## Decode the opportunity

Use `references/decoder-fields.md` and capture, where applicable:

- programme, pillar, cluster, destination, call, and topic identifier
- plain-language problem, expected outcomes, scope, and exclusions
- opening date, deadline or stages, and current portal status
- action type, funding model/rate, total topic budget, expected contribution per project, and indicative project count
- expected starting and ending TRL, demonstrations, standards, data, facilities, or end-user requirements
- consortium rule, applicant-country rule, participation restrictions, funding eligibility, and intended participant role
- lump-sum or actual-cost treatment and the required budget/application templates
- security, ethics, open-science, gender-dimension, data-management, or dissemination conditions
- named partnerships, mandatory coordination, portfolio obligations, or dependencies on EU infrastructure

### Hard-gate checks

- Distinguish a `call` from a `topic`; do not merge their identifiers, dates, budgets, or conditions.
- Treat the often-quoted three-organisation rule as a general default with exceptions. Verify the exact topic.
- Check both permission to participate and eligibility to receive EU funding. They are not equivalent.
- Check the current status of every relevant country and the exact role proposed for the organisation.
- Inspect Article 22(5) or other topic-specific participation restrictions. Space topics can be much narrower than the programme-wide default.
- Check whether ownership/control restrictions, security scrutiny, classified information, or limited dissemination apply. Do not treat ordinary commercial confidentiality as EU classified information.
- Check whether the topic is lump sum and whether the current detailed budget workbook applies.
- Treat a failed eligibility, country, consortium, security, deadline, or scope gate as red even when thematic fit is high.

## Opportunity scan

1. Search broadly enough to catch synonyms, acronyms, enabling technologies, application areas, and adjacent destinations.
2. Deduplicate by exact topic identifier.
3. Apply hard gates before ranking thematic fit.
4. Produce a compact shortlist with:
   - topic identifier and title
   - current status and deadline
   - action type, contribution range, TRL, and consortium/participation conditions
   - fit rationale and evidence
   - hard blockers and unknowns
   - direct official topic URL
5. Include excluded near-matches when their exclusion teaches the user something important, such as a country restriction or an incompatible TRL.

## Strategic fit

Use `templates/company-profile.md` to normalise each organisation before comparing it with topics.

- Assess mission fit, capability fit, evidence/track-record fit, TRL fit, consortium-role fit, funding/eligibility fit, timing, and proposal effort separately.
- Use `green`, `amber`, `red`, or `unknown` with a short evidence-backed reason. Do not hide hard gates in a weighted score.
- Separate what the organisation can contribute from what it would need from partners.
- Label conclusions based only on public company information as provisional.
- Return a portfolio view only after each topic has an individual hard-gate review.

## Application map

For a confirmed target:

1. Obtain the topic's current submission documents from the live portal.
2. Map expected outcomes and scope requirements to the current Part B sections: Excellence, Impact, and Quality and efficiency of implementation.
3. Map work packages, participant roles, person-months, direct costs, indirect costs, equipment/depreciation, subcontracting, and justifications to the current budget template.
4. Reconcile participant names, work-package identifiers, person-months, and cost totals across Part A, Part B, and the detailed budget workbook.
5. Record page limits, annex rules, evaluation criteria, and any topic-specific deviations exactly from current documents.
6. Produce an evidence request list and owner for every unsupported claim or missing input.
7. Do not modify an official macro-enabled workbook casually. Preserve the original, inspect instructions and formulas, and use the workbook's documented export route for submission.

## Output

Use `templates/opportunity-brief.md` for a single-topic or go/no-go brief. Keep the result decision-oriented:

- answer the user's question first
- show hard gates before attractive narrative
- cite every deadline, eligibility, funding, TRL, consortium, and security claim near the claim
- give an explicit `pursue`, `pursue if`, `monitor`, or `do not pursue` recommendation when the user asks for a decision
- finish with unresolved questions, required owners, and the next evidence-gathering action

Never claim that a topic is open, an organisation is eligible, funding is available, or an application is submission-ready unless the current official evidence has been checked.
