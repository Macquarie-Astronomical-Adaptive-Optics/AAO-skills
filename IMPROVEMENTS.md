# IMPROVEMENTS.md

*Analysis date: 2026-07-11*

AAO-skills is a Claude Code plugin marketplace (plus a Codex symlink installer) containing ten reusable skills for AAO work: AARC grant writing, paper downloading, and a cluster of telescope/space-instrument concept-verification skills. It is young (three commits, v0.1.0, last touched 2026-05-05), structurally clean, and mostly scaffolding: every skill is a single SKILL.md checklist, and every `references/`, `templates/`, `scripts/`, and `evals/` directory contains only a `.gitkeep`. The working tree is clean. The main gap is not bugs but hollowness — the skills describe workflows without shipping any of the supporting material they reference.

## Bugs & Fixes

- **Skills reference directories that are empty.** `aarc-grant-writing/SKILL.md` tells the agent to "Use files in `references/` and `templates/`" and `paper-downloading` has a `scripts/` dir — all contain only `.gitkeep`. An agent following the skill will look for material that doesn't exist. Either populate these (see Improvements) or strip the references until content lands.
- **`install/install-codex.sh` never removes stale symlinks.** If a skill is renamed or deleted, old symlinks in `~/.agents/skills` dangle forever. Add a cleanup pass (e.g. remove symlinks in `$DEST` that point into `$SRC` but no longer resolve) or an `--uninstall` flag.
- **No guard against running install-codex.sh from a moved/deleted checkout.** Symlinks point into the repo; if the repo moves, all ten skills silently break. At minimum, echo the source path and note this in `install/install-claude-code.md`.

## Improvements (prioritized)

1. **Ship the reference material the skills promise.** Highest value: `aarc-grant-writing/references/` (AARC scheme criteria summaries, assessment rubric notes) and `templates/` (Markdown brief template matching the workflow's "working Markdown brief" step). The workflow is good; the template would make it repeatable.
2. **Add scripts to `paper-downloading/scripts/`.** A small `uv`-runnable Python script for arXiv/ADS/DOI fetching with provenance capture (BibTeX + source URL + download date) would turn a 63-line checklist into a working tool. Use `pyproject.toml` + `uv add` — do not introduce a requirements.txt.
3. **Write evals.** Every skill has an empty `evals/` dir. Even 2–3 scenario prompts per skill (input + expected behavior notes) would let you regression-test skill quality with the skill-creator tooling.
4. **Consider merging near-duplicate skills.** `telescope-creation` (20 lines) overlaps heavily with `space-telescope-concept`; `infrared-shaped-mirror` (20 lines) is thin. Either flesh them out with actual optics formulas/scripts or fold them into the larger skills to reduce trigger ambiguity.
5. **Tighten skill descriptions for triggering.** Several descriptions are long single sentences; the "Use when..." clause is what drives skill selection. Test triggering accuracy (skill-creator has a benchmark mode).

## Testing

- No CI at all. Add a GitHub Actions workflow that: validates `marketplace.json` and `plugin.json` against the plugin schema (or at least `jq` parses them), checks every skill dir has a SKILL.md with valid frontmatter (`name` matching the directory, non-empty `description`), and shellchecks `install/install-codex.sh`.
- A tiny frontmatter-lint script (uv-run Python) would also catch drift between the README skill table and the actual `plugins/aao-skills/skills/` contents.

## Documentation

- README's skill table must be kept in sync with the skills dir — currently it matches, but there's no check. Note this in a CONTRIBUTING section or automate it.
- `CHANGELOG.md` stops at 0.1.0 but commit `4e30215` ("Expand AAO skill workflows") post-dates it; add a 0.1.1 entry or an Unreleased section.
- Document the versioning/release process: `version` appears in both `.claude-plugin/marketplace.json` and `plugins/aao-skills/.claude-plugin/plugin.json` and must be bumped in both — easy to miss.

## Security

- No secrets or credentials found; SECURITY.md and the restricted-material boundary are well handled. Good.
- Consider a pre-commit or CI grep (e.g. gitleaks) as a belt-and-braces check, since this repo's whole premise is "safe for broad circulation" — an automated screen for obvious markers (emails, partner names list, "restricted", credentials) would enforce the SECURITY.md policy mechanically.

## Housekeeping / Modernization

- Bump plugin version when workflows change; the marketplace caches by version.
- Add a LICENSE header check — LICENSE exists (477 bytes) but README doesn't state the license; mention it.
- Remove `.gitkeep` files as directories gain real content.

## Quick Wins

- Add an "Unreleased" section to CHANGELOG.md covering commit `4e30215`.
- Add stale-symlink cleanup to `install/install-codex.sh` (~5 lines).
- Add a Markdown grant-brief template to `aarc-grant-writing/templates/` — the workflow already specifies its sections (criteria, idea, capability story, plan, risks, budget assumptions, open questions, source facts).
- Add a one-line license statement to README.
