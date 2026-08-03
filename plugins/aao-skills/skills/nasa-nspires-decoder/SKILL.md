---
name: nasa-nspires-decoder
description: Decode NASA research funding through NSPIRES, ROSES, NASA Research Announcements, and related Grants.gov submissions. Use when finding NASA space or Earth-science opportunities, interpreting a ROSES program element, checking foreign-organisation eligibility, deadlines, registrations, or preparing an evidence-backed NASA solicitation brief.
---

# NASA NSPIRES Decoder

Turn a NASA research announcement or ROSES program element into an auditable opportunity brief. Treat NSPIRES as a solicitation, registration, proposal, and peer-review system—not as proof that every listed opportunity funds every applicant type.

## Safety and scope

- Keep unpublished proposal strategy, partner-private information, export-controlled technical data, CUI, and security-sensitive details out of this repository.
- Move controlled or clearance-dependent material to the restricted workflow.
- Use public capability descriptions or anonymised organisation profiles for exploratory matching.
- Distinguish research grants/cooperative agreements, challenges, RFIs, contracts, and mission acquisitions. Do not apply ROSES rules to every NASA opportunity.

## Choose the mode

1. `Opportunity scan`: search open and future NASA research announcements or current ROSES program elements.
2. `Program-element decoder`: explain one exact opportunity and its deviations from the master solicitation.
3. `Foreign-participation check`: determine whether and how a non-US organisation or researcher may participate and be funded.
4. `Application map`: map a confirmed opportunity to NSPIRES/Grants.gov registrations, submission stages, forms, and evidence.

## Source-first workflow

1. Read `references/source-hierarchy.md`.
2. Establish a dated source snapshot with solicitation number, program-element identifier, amendment/version, access time, and direct URL.
3. Open the current NSPIRES opportunity record and download its current solicitation documents.
4. If it is a ROSES element, read both:
   - the current ROSES Summary of Solicitation and tables; and
   - the program element, including every amendment, clarification, and special condition.
5. Check the NASA Science funding-opportunities page and relevant ROSES amendment/blog page for changes.
6. Verify registration and submission instructions against current NSPIRES guidance. If Grants.gov is allowed or required, check that route separately.
7. Keep evidence states distinct: `confirmed`, `inferred`, and `unknown`.

An old ROSES PDF, a remembered annual date, or an NSPIRES cycle end date is not proof of the current deadline for a program element.

## Decode the opportunity

Capture:

- solicitation title and number, sponsoring NASA organisation, cycle, and program element
- opportunity type: grant, cooperative agreement, challenge, RFI, contract, or other
- current state: future, open, amended, due soon, rolling/no-fixed-date, closed, or unclear
- NOI, Step-1, Step-2, full-proposal, and other dates, with timezone and whether each stage is mandatory
- objectives, science/technology scope, exclusions, expected deliverables, duration, and review criteria
- applicant and organisation eligibility, including foreign-organisation treatment
- PI, co-I, collaborator, subaward, NASA civil-servant, and institutional roles
- award range or ceiling, cost sharing, restrictions, period of performance, and allowability references
- required registrations: individual NSPIRES account, organisation affiliation, AOR, SAM/UEI, and Grants.gov where applicable
- proposal sections, page limits, budget forms, data/open-science plans, facilities, letters, certifications, and electronic submission route
- export control, CUI, national-security, China-related statutory restrictions, or other special conditions when the source invokes them
- program officer and technical/help-desk contact routes

## Hard gates for Australian participation

- Read the exact eligibility section; do not generalise from another ROSES element or year.
- Separate permission for a foreign researcher to join a team from eligibility of a foreign organisation to receive NASA funds.
- Identify any no-exchange-of-funds, direct-funding, subaward, bilateral-agreement, or partner-agency route exactly as the solicitation states it.
- Confirm whether a US proposing organisation is required and whether the Australian institution can be a subrecipient, collaborator, or unfunded partner.
- Check SAM/UEI, NSPIRES organisation registration, AOR, and team-member registration early enough to submit.
- Treat export-control, CUI, nationality, and statutory restrictions as hard gates. Do not infer that ordinary academic publication resolves them.
- Confirm that the deadline is a real proposal date, not the end of the umbrella solicitation or a placeholder shown for a rolling program.

## Opportunity scan

1. Search NSPIRES `OPEN`, `FUTURE`, and relevant due-date listings using mission, science, instrument, technology, and application synonyms.
2. Search current ROSES subject tables and funding-opportunity pages.
3. Deduplicate by exact solicitation/program-element identifier.
4. Apply eligibility and foreign-participation gates before ranking scientific fit.
5. Return direct official links and include excluded near-matches when they reveal a decisive restriction.

## Application map

For a confirmed target:

1. Identify every submission stage and institutional approver.
2. Build a registration-readiness checklist for the investigator, organisation, AOR, SAM/UEI, NSPIRES, and Grants.gov if applicable.
3. Map the current solicitation's required sections, forms, page limits, attachments, and naming rules.
4. Map objectives and evaluation factors to claims, evidence, tasks, schedule, team, budget, and risk controls.
5. Record every program-element deviation from the ROSES summary or general NASA guidance.
6. Reconcile people, roles, organisations, budgets, dates, and attachments across every submission surface.

## Output

Use `templates/nasa-opportunity-brief.md`. Lead with the feasible participation route and any hard blocker. Give `pursue`, `pursue if`, `monitor`, or `do not pursue` only when requested.

Cite eligibility, foreign funding, dates, submission stages, registrations, funding, and special restrictions near each claim. Never claim that a proposal is submission-ready from a document review alone; the live NSPIRES workspace and institutional release remain separate checks.
