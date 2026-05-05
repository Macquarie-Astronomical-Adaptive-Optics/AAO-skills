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
- `paper-downloading`
- `infrared-shaped-mirror`
- `telescope-creation`

Keep restricted or Defence-specific material out of this repository. Use `AAO-restricted-skills` for that content.
