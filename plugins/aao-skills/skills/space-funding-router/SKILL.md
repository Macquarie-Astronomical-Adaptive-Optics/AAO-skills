---
name: space-funding-router
description: Find, compare, and route space-project funding opportunities across Horizon Europe, NASA NSPIRES/ROSES, ESA OSIP/esa-star, and Australian Space Agency or GrantConnect sources. Use when a user asks where a space, astronomy, telescope, instrumentation, Earth-observation, communications, launch, or space-technology project could be funded, or wants a cross-portal shortlist.
---

# Space Funding Router

Turn a project concept into a source-backed cross-platform funding scan. This skill chooses the correct specialist decoder; it does not replace the rules of any funding system.

## Safety and evidence boundary

- Use only public or user-approved project information in broadly shareable outputs.
- Keep unpublished technical strategy, named-partner weaknesses, export-controlled information, Defence priorities, security classifications, and internal go/no-go decisions out of this repository.
- Move controlled, Defence-adjacent, clearance-dependent, or partner-private work to the restricted workflow.
- Treat a portal listing, aggregator, search result, newsletter, or model answer as discovery evidence only.
- Never describe an organisation as eligible, a call as open, or money as available until the current official source has been checked.

## Minimum project profile

Use available context before asking questions. Establish:

- applicant legal entity and country of establishment
- university, research institute, company, government body, consortium, or individual
- intended role: lead, prime, coordinator, beneficiary, partner, subcontractor, collaborator, or unknown
- project type: basic research, instrument, mission concept, technology maturation, demonstration, infrastructure, service, commercialisation, or procurement supply
- domain, problem, capabilities, evidence, starting and target TRL
- approximate funding need, co-funding capacity, start window, duration, and deadline tolerance
- known partners, required geography, export/security concerns, and confidentiality classification

Mark any missing fact that could reverse eligibility as a `hard unknown`.

## Route by platform

Read `references/portal-map.md`, then use every relevant specialist skill:

- `horizon-europe-decoder`: collaborative European research and innovation topics, including Cluster 4 Space and related infrastructure or digital calls.
- `nasa-nspires-decoder`: NASA research announcements and ROSES program elements submitted through NSPIRES or Grants.gov.
- `esa-space-funding-decoder`: ESA ideas, research, technology-development, business-application, and tender routes through OSIP and esa-star.
- `australian-space-funding-decoder`: Australian Space Agency and Commonwealth grant routes, including GrantConnect, business.gov.au, and relevant ARC schemes.

Do not force a project into all four. Include a portal only when its instrument, geography, maturity, and timing are plausible.

## Cross-platform workflow

1. Record an access-dated source snapshot for each portal inspected.
2. Search using mission outcomes, enabling technology, end users, science questions, application sectors, and synonyms—not only the project name.
3. Identify the exact opportunity identifier and instrument type.
4. Apply hard gates before thematic ranking:
   - legal-entity and country eligibility
   - lead/prime/coordinator eligibility
   - partner and consortium structure
   - funding versus participation distinction
   - co-funding or no-exchange-of-funds rule
   - TRL, scope, mission, and end-user fit
   - opening/deadline and registration readiness
   - security, export, ownership/control, nationality, or procurement restrictions
5. Compare only opportunities that survive or plausibly survive the hard gates.
6. Use `templates/cross-platform-scan.md` for the result.

## Comparison dimensions

Keep these fields separate rather than collapsing them into one score:

- scientific or strategic fit
- technology and TRL fit
- allowed instrument: research grant, cooperative agreement, co-funded development, contract/tender, loan/equity, or support program
- applicant geography and legal-entity fit
- feasible role for the organisation
- consortium and partner burden
- funding amount, rate, co-funding, and eligible-cost fit
- timing and registration readiness
- proposal effort and evidence maturity
- security/export/control risks
- current-source confidence

A failed hard gate remains red even when scientific fit is excellent.

## Output

Lead with a compact portfolio:

- `pursue`: hard gates checked and fit is strong
- `pursue if`: promising, with named hard conditions to resolve
- `monitor`: strategically relevant but unavailable, immature, or poorly timed
- `do not pursue`: a confirmed hard gate or material scope mismatch

For each candidate include the portal, exact identifier/title, instrument, current status and deadline, likely role, funding/co-funding model, hard gates, rationale, direct official URL, evidence status, and next action.

Finish with:

- excluded near-matches and why they failed
- unresolved facts and their owners
- registrations or institutional approvals needed
- the next official document or portal page to inspect

Do not start an application merely because the cross-platform scan finds a thematic match.
