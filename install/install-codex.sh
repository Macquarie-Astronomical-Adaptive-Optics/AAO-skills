#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/plugins/aao-skills/skills"
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"
for skill in "$SRC"/*; do
  name="$(basename "$skill")"
  ln -sfn "$skill" "$DEST/$name"
done
echo "Installed AAO skills into $DEST"
