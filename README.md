# AAO Skills

## Install First

New to Codex at AAO? Follow the [AAO Codex onboarding guide](install/aao-codex-onboarding.md) for the complete setup, including Git, GitHub and GitLab access, Office integration, OneDrive indexing, the weekly skills updater, and a first automation project.

In Claude Code, run these commands one at a time.

```text
/plugin marketplace add Macquarie-Astronomical-Adaptive-Optics/AAO-skills
```

Then run:

```text
/plugin install aao-skills@aao-skills-marketplace
```

For one local installation used automatically by both Claude Code and Codex on macOS or Linux, run from this repository root:

```bash
./install/install-agent-skills.sh
```

This links the same canonical skill folders into Claude Code's `~/.claude/skills` and Codex's `~/.agents/skills`. There is only one copy of each `SKILL.md` to maintain.

On Windows, run:

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\install\install-agent-skills.ps1
```

The Windows installer avoids symlink and Developer Mode requirements. It creates marked, generated copies under `%USERPROFILE%\.claude\skills` and `%USERPROFILE%\.agents\skills`; rerun it after updating the repository. It will refresh only copies bearing its management marker and will not replace an unrelated existing skill directory.

For a Codex-only installation, run:

```bash
./install/install-codex.sh
```

Reusable AAO skills for grant and opportunity analysis, research-paper handling, optics, telescope design, and concept verification.

This repository is for broadly shareable material that can circulate inside AAO and with approved collaborators. It must not contain restricted examples, reviewer notes, partner-private information, Defence priorities, internal strategy, clearance assumptions, controlled data, or commercially sensitive project details.

The internal shape mirrors `AAO-restricted-skills` so users can move between the two repositories without learning a second convention.

## Layout

```text
AAO-skills/
  install/
  .claude-plugin/
  plugins/
    aao-skills/
      .claude-plugin/
      skills/
```

## Skills

| Skill | Scope |
| --- | --- |
| `aarc-grant-writing` | Broadly shareable AARC-style grant drafting and review. |
| `horizon-europe-decoder` | Source-bound Horizon Europe opportunity discovery, eligibility checks, strategic fit, and application mapping. |
| `space-funding-router` | Cross-platform triage and comparison across Horizon Europe, NASA, ESA, and Australian space-funding systems. |
| `nasa-nspires-decoder` | NASA NSPIRES and ROSES solicitation discovery, program-element decoding, eligibility gates, and application mapping. |
| `esa-space-funding-decoder` | ESA OSIP, esa-star, and related funding or tender route decoding with geography and co-funding gates. |
| `australian-space-funding-decoder` | Australian Space Agency, GrantConnect, business.gov.au, and relevant ARC space-funding discovery and decoding. |
| `paper-downloading` | Legal paper acquisition, organization, and provenance capture. |
| `infrared-shaped-mirror` | General infrared shaped-mirror notes, calculations, and scripts. |
| `telescope-creation` | General telescope design and proposal-development support. |
| `space-telescope-concept` | Space-telescope concept studies with optical, mission, thermal, launch, radiation, and verification assumptions. |
| `telescope-geometry-honesty` | Geometry, CAD-like export, and render checks for physically credible telescope concept models. |
| `thermal-optical-mechanical-closure` | STOP-style screening that links thermal cases, structural deformation, and optical performance. |
| `space-environment-screening` | Orbit, thermal, radiation, contamination, survival, and operations screening for space instruments. |
| `requirements-budget-verification` | Traceable requirements, budgets, verification matrices, test plans, and release gates. |
| `manufacturing-package-sanity` | BOM, drawing, material, interface, tolerance, assembly, and inspection checks for concept manufacturing packages. |

## Restricted-Material Boundary

If a task needs sensitive, Defence-adjacent, security-sensitive, commercially sensitive, controlled, partner-private, or clearance-dependent information, use `../AAO-restricted-skills` instead.
