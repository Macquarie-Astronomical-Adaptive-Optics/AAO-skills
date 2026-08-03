#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/plugins/aao-skills/skills"
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"
for skill in "$SRC"/*; do
  [[ -d "$skill" && -f "$skill/SKILL.md" ]] || continue
  name="$(basename "$skill")"
  link="$DEST/$name"
  if [[ -L "$link" ]]; then
    ln -sfn "$skill" "$link"
  elif [[ -e "$link" ]]; then
    printf 'Skipped %s: %s already exists and is not a symlink.\n' "$name" "$link" >&2
  else
    ln -s "$skill" "$link"
  fi
done
echo "Installed AAO skills into $DEST"
