#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from doc_tokens import approx_tokens, iter_files  # noqa: E402


# Growth-friendly defaults for ongoing projects.
DEFAULT_BUDGET = 40000
DEFAULT_WARN_RATIO = 0.75


def main() -> int:
    budget = int(os.getenv("DOC_TOKEN_BUDGET", str(DEFAULT_BUDGET)))
    warn_ratio = float(os.getenv("DOC_TOKEN_WARN_RATIO", str(DEFAULT_WARN_RATIO)))
    warn_tokens = int(budget * warn_ratio)

    files = list(iter_files())
    per_file: list[tuple[Path, int]] = []
    total = 0

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        tokens = approx_tokens(text)
        per_file.append((path, tokens))
        total += tokens

    per_file.sort(key=lambda x: x[1], reverse=True)

    if total >= budget:
        status = "EXCEEDED"
    elif total >= warn_tokens:
        status = "WARN"
    else:
        status = "OK"

    print(f"status: {status}")
    print(f"total_tokens: {total}")
    print(f"budget_tokens: {budget}")
    print(f"warn_tokens: {warn_tokens}")
    print(f"default_budget_tokens: {DEFAULT_BUDGET}")
    print(f"default_warn_ratio: {DEFAULT_WARN_RATIO}")
    print("override_env: DOC_TOKEN_BUDGET, DOC_TOKEN_WARN_RATIO")
    print("top_files:")
    for path, tokens in per_file[:5]:
        print(f"- {path}: {tokens}")

    if status == "WARN":
        print("action_required:")
        print("- Run lightweight non-destructive cleanup.")
        print("- Remove obvious duplication via links/summaries (no deletion).")
        print("- Keep all core foundation/design/guideline sections untouched.")
    elif status == "EXCEEDED":
        print("action_required:")
        print("- Run full document review for duplication and stale details.")
        print("- Propose deletion/truncation candidates with impact and token savings.")
        print("- Ask user approval before any removal/truncation.")
        print("- Never delete/trim core foundation/design/guideline sections.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
