# AAO Skills

Reusable AAO skills for grant writing, research-paper handling, optics, and telescope design.

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

## Install

For Codex-compatible local skill discovery:

```bash
./install/install-codex.sh
```

For Claude Code plugin setup, use `.claude-plugin/marketplace.json` as the local marketplace entrypoint. See `install/install-claude-code.md`.

## Restricted-Material Boundary

If a task needs sensitive, Defence-adjacent, security-sensitive, commercially sensitive, controlled, partner-private, or clearance-dependent information, use `../AAO-restricted-skills` instead.
