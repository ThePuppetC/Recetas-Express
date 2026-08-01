#!/bin/bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Este script debe ejecutarse dentro de un repositorio git."
  exit 1
fi

if [[ $# -gt 1 ]]; then
  echo "Uso: ./auto_commit.sh [mensaje]"
  exit 1
fi

MESSAGE="${1:-auto-commit: cambios actualizados}"

git add -A

git diff --cached --quiet
if [ $? -eq 0 ]; then
  echo "No hay cambios nuevos para guardar."
  exit 0
fi

git commit -m "$MESSAGE"
git push

echo "Commit creado y enviado correctamente."
