# AAO Skills

## Install First

In Claude Code, run these commands one at a time.

```text
/plugin marketplace add Macquarie-Astronomical-Adaptive-Optics/AAO-skills
```

Then run:

```text
/plugin install aao-skills@aao-skills-marketplace
```

For Codex, run from this repository root:

```bash
./install/install-codex.sh
```

Reusable AAO skills for grant writing, research-paper handling, optics, telescope design, and concept verification.

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
