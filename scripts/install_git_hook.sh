#!/bin/sh
set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$ROOT_DIR"
chmod +x .githooks/pre-commit
git config core.hooksPath .githooks

echo "Installed git hooks path: .githooks"
echo "pre-commit hook enabled: python3 scripts/check_arch.py"
echo "pre-commit hook enabled: python3 scripts/check_docs.py"
