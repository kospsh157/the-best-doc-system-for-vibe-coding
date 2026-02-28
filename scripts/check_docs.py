#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

DOC_PATHS = [
    ROOT_DIR / "starter.md",
    *(ROOT_DIR / "docs").rglob("*.md"),
]

EXCLUDED_FILES = {
    "docs/specs/TEMPLATE.md",
    "docs/architecture/adr/0000-template.md",
}

REQUIRED_TEXT = {
    "starter.md": [
        "## 사용자 호출 문구 대응(고정)",
        "## 3단계 운영 프로토콜(필수)",
        "## 주제 확정 이후 전환 규칙(필수)",
        "## 토큰 관리 및 안전 축약 규칙(필수)",
    ],
    "docs/README.md": [
        "## 주 목적 (필수)",
        "## AI 복귀 정보 맵 (필수)",
        "## 주제 확정 후 문서 운영 (필수)",
        "## 토큰 예산 운영 원칙 (필수)",
    ],
    "docs/session/README.md": [
        "## AI 빠른 복귀 체크 (60초)",
        "## 세션 운영 프로토콜 (고정)",
        "## 주제 수령 시 즉시 실행 (필수)",
        "## 문서 축약 안전장치 (필수)",
    ],
    "docs/session/LOG.md": [
        "## 항목 템플릿",
        "- 재개 포인트:",
    ],
    "docs/session/END_PROMPT.md": [
        "재개 포인트 항목",
    ],
}

BANNED_PHRASES = {
    "starter.md": ["최신 항목만"],
    "docs/README.md": ["최신 항목만"],
    "docs/session/README.md": ["최신 항목만"],
}

PLACEHOLDER_BULLET_RE = re.compile(r"^\s*-\s*$")
PENDING_BULLET_RE = re.compile(r"^\s*-\s*\(추가 예정\)\s*$")


def rel_path(path: Path) -> str:
    return str(path.relative_to(ROOT_DIR))


def should_skip(path: Path) -> bool:
    return rel_path(path) in EXCLUDED_FILES


def check_file_content(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    relative = rel_path(path)

    for line_no, line in enumerate(text.splitlines(), 1):
        if PLACEHOLDER_BULLET_RE.match(line):
            errors.append(f"{relative}:{line_no} empty bullet placeholder is not allowed")
        if PENDING_BULLET_RE.match(line):
            errors.append(f"{relative}:{line_no} '(추가 예정)' placeholder bullet is not allowed")

    for required in REQUIRED_TEXT.get(relative, []):
        if required not in text:
            errors.append(f"{relative} missing required text: {required}")

    for phrase in BANNED_PHRASES.get(relative, []):
        if phrase in text:
            errors.append(f"{relative} contains banned phrase: {phrase}")

    return errors


def main() -> int:
    files: list[Path] = []
    for path in DOC_PATHS:
        if path.is_file() and not should_skip(path):
            files.append(path)

    files = sorted(set(files))

    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        errors.extend(check_file_content(path, text))

    if errors:
        print("Documentation quality check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation quality check passed ({len(files)} files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
