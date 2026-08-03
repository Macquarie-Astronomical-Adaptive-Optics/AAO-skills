# Installing for Claude Code

Use the repository marketplace file as the Claude Code local marketplace entrypoint:

```text
.claude-plugin/marketplace.json
```

The marketplace points at:

```text
./plugins/aao-skills
```

After configuring the marketplace in Claude Code, confirm that the `aao-skills` plugin appears with the expected skills:

- `aarc-grant-writing`
- `horizon-europe-decoder`
- `space-funding-router`
- `nasa-nspires-decoder`
- `esa-space-funding-decoder`
- `australian-space-funding-decoder`
- `paper-downloading`
- `infrared-shaped-mirror`
- `telescope-creation`

## One canonical tree for Claude Code and Codex

For a local installation shared by both products on macOS or Linux, run from the repository root:

```bash
./install/install-agent-skills.sh
```

The script creates symlinks in both `~/.claude/skills` and `~/.agents/skills`. Each link points to the corresponding canonical folder under `plugins/aao-skills/skills`, so Claude Code and Codex read the same `SKILL.md`, references, templates, and scripts.

The installer does not replace a real file or directory already present at either destination. It reports the collision and leaves it alone.

On Windows, use the copy-based installer:

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\install\install-agent-skills.ps1
```

Windows does not reliably permit portable symlink creation across machines. The PowerShell installer therefore treats `plugins/aao-skills/skills` as the single authored source and creates marked copies in `%USERPROFILE%\.claude\skills` and `%USERPROFILE%\.agents\skills`. Rerunning it refreshes only installer-managed copies; unrelated existing directories are skipped.

Keep restricted or Defence-specific material out of this repository. Use `AAO-restricted-skills` for that content.
