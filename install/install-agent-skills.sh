#!/usr/bin/env bash
set -euo pipefail

AAO_SKILLS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AAO_SKILLS_SOURCE="$AAO_SKILLS_ROOT/plugins/aao-skills/skills"
AAO_CODEX_DEST="${AAO_CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
AAO_CLAUDE_DEST="${AAO_CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

install_skills() {
  local product="$1"
  local destination="$2"
  local skill
  local name
  local link

  mkdir -p "$destination"
  for skill in "$AAO_SKILLS_SOURCE"/*; do
    [[ -d "$skill" && -f "$skill/SKILL.md" ]] || continue
    name="$(basename "$skill")"
    link="$destination/$name"

    if [[ -L "$link" ]]; then
      ln -sfn "$skill" "$link"
    elif [[ -e "$link" ]]; then
      printf 'Skipped %s for %s: %s already exists and is not a symlink.\n' "$name" "$product" "$link" >&2
      continue
    else
      ln -s "$skill" "$link"
    fi
  done
  printf 'Installed AAO skill links for %s in %s\n' "$product" "$destination"
}

install_skills "Codex" "$AAO_CODEX_DEST"
install_skills "Claude Code" "$AAO_CLAUDE_DEST"

printf 'Both products now read the same canonical skill folders under %s\n' "$AAO_SKILLS_SOURCE"
