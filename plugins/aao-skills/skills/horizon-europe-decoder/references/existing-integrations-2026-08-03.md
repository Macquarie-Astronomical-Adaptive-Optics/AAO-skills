# Existing Horizon Europe integrations survey — 2026-08-03

## Question

Is there an existing MCP server or reusable agent skill that should replace or complement the local `horizon-europe-decoder`?

## Finding

The targeted search found a useful official API surface, two relevant third-party hosted MCP servers, and community Agent Skills that mention or focus on Horizon Europe. It did not find an official Horizon-Europe-specific MCP server or Agent Skill, nor a community project that provides the same source-bound document-analysis workflow as this skill.

This is a dated discovery result, not a permanent claim that no other project exists.

## Official foundation

### EU Funding & Tenders Portal public APIs

- Official entry point: https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/support/apis
- Best use: programmatic discovery of portal topics and records, followed by opening the canonical topic page and current documents.
- Status: preferred machine-readable foundation because the European Commission controls it.
- Limitation: an API record does not perform organisation-specific eligibility analysis or replace topic documents, annexes, updates, and submission templates.

## Third-party hosted MCP servers

### EUACC

- Product page: https://www.euacc.ai/ai-tools
- Remote endpoint advertised by the provider: `https://www.euacc.ai/api/mcp`
- Advertised coverage: EU Funding & Tenders, CORDIS, Horizon Europe, EIC, Digital Europe, partner discovery, and related EU datasets.
- Access model: account and connector key.
- Audit boundary: hosted service; no local implementation was identified in this survey.
- Caution: the inspected product page displayed differing open-call totals in different sections. Treat freshness and reconciliation as claims to test, not facts to inherit.

### GrantIQ

- Documentation repository: https://github.com/akis111/grantiq-mcp
- Remote endpoint advertised by the provider: `https://grantiq.co.uk/mcp`
- Advertised coverage: UK and EU grant discovery, organisation profiles, eligibility matching, opportunity explanation, and cited funder pages.
- Access model: hosted OAuth service with usage limits.
- Audit boundary: the public repository is an installation/documentation shell; it says the server itself is hosted, so the matching implementation cannot be reviewed there.
- Maturity signal at inspection: four commits and no public stars or forks. This is not a quality verdict, but it supports a cautious pilot rather than immediate operational dependence.

## Community Agent Skills

GitHub code search returned many `SKILL.md` matches containing “Horizon Europe”. The raw count is not a count of distinct, working Horizon skills: it includes generic research skills, registry copies, forks, and incidental mentions. Two direct examples were inspected at fixed revisions.

### `eu-horizon-guide`

- Source: https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/research/funding/eu-horizon-guide/SKILL.md
- Contents at inspection: one `SKILL.md`; no parser, source snapshots, templates, or tests in the skill directory.
- Strength: a readable general primer on programme structure, consortium building, budgeting, evaluation, and proposal writing.
- Limitations for AAO: it presents programme-wide defaults and rules without source dates or call-level citations; several statements are broad enough that they must not be inherited as live eligibility or proposal rules. It does not ingest or reconcile a supplied call document.
- Best use: background orientation only, after current official sources are checked.

### `eu-grant-hunter`

- Registry copy: https://github.com/majiayu000/claude-skill-registry/blob/108064e782d02f455fb627e7b0ca2c5d7494da18/skills/data/eu-grant-hunter/SKILL.md
- Declared upstream: https://github.com/PandaAllIn/UBOS_FINAL/blob/main/trinity/skills/deployment/janus-haiku-skills-v1.0/skills/eu-grant-hunter/SKILL.md
- Contents at inspection: the registry directory contains `SKILL.md` and provenance metadata, but none of the scanner, scoring, reminder, dashboard, or communications scripts named by the instructions.
- Fit: heavily specialised to another organisation's capability model, server paths, automation protocol, pipeline value, and internal roles. It is not a portable working implementation in the inspected copy.
- Licensing: registry metadata marks the upstream permission as restricted or unknown. Do not copy its text or design into this repository without resolving permission.

These examples confirm that reusable Horizon-oriented instructions exist online. They do not remove the need for the AAO decoder's exact-document identity checks, evidence ledger, Australian participation/funding distinction, regression cases, and parser.

## Recommendation

1. Keep the local skill as the decision and evidence layer.
2. Prefer the official EU API for discovery work that needs automation.
3. If a hosted MCP is trialled, use a read-only test profile with no unpublished project strategy or partner-private data.
4. Evaluate it against fixed cases from `evals/cases.md`: exact topic identity, live status, Australian participation and funding eligibility, Article 22(5) restrictions, action type, deadline, and source URLs.
5. Retain the canonical portal page and current documents as the authority even when an MCP returns a confident answer.
6. Treat community skills as design references to inspect, not trusted dependencies; verify provenance, licence, bundled files, and current programme rules before reuse.

Do not add either hosted MCP to the plugin until its authentication, privacy terms, data provenance, failure behaviour, and test results have been reviewed.
