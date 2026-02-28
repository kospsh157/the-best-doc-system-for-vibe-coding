#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"

SOURCE_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}
LAYER_RULES = {
    "domain": {"domain"},
    "application": {"domain", "application"},
    "interface": {"domain", "application", "interface"},
    "infrastructure": {"domain", "application", "infrastructure"},
    "entrypoints": {"domain", "application", "interface", "entrypoints"},
}

JS_IMPORT_RE = re.compile(
    r"(?:import|export)\s+(?:type\s+)?(?:[^'\"]*?\s+from\s+)?['\"]([^'\"]+)['\"]"
    r"|require\(\s*['\"]([^'\"]+)['\"]\s*\)"
)
PY_FROM_RE = re.compile(r"^\s*from\s+([A-Za-z0-9_\.]+)\s+import\s+")
PY_IMPORT_RE = re.compile(r"^\s*import\s+(.+)$")


def iter_source_files() -> list[Path]:
    if not SRC_DIR.exists():
        return []
    files: list[Path] = []
    for path in SRC_DIR.rglob("*"):
        if path.is_file() and path.suffix in SOURCE_EXTENSIONS:
            files.append(path)
    return sorted(files)


def layer_from_path(path: Path) -> str | None:
    try:
        rel = path.relative_to(SRC_DIR)
    except ValueError:
        return None
    if not rel.parts:
        return None
    layer = rel.parts[0]
    if layer not in LAYER_RULES:
        return None
    return layer


def parse_import_specs(path: Path, text: str) -> list[tuple[int, str]]:
    specs: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if path.suffix == ".py":
            from_match = PY_FROM_RE.match(line)
            if from_match:
                specs.append((lineno, from_match.group(1).strip()))
                continue

            import_match = PY_IMPORT_RE.match(line)
            if import_match:
                raw = import_match.group(1).split("#", 1)[0]
                for part in raw.split(","):
                    item = part.strip().split(" as ", 1)[0].strip()
                    if item:
                        specs.append((lineno, item))
            continue

        for match in JS_IMPORT_RE.finditer(line):
            spec = match.group(1) or match.group(2)
            if spec:
                specs.append((lineno, spec.strip()))

    return specs


def resolve_relative_path_layer(file_path: Path, spec: str) -> str | None:
    target = Path(os.path.normpath(str(file_path.parent / spec)))
    try:
        rel = target.relative_to(SRC_DIR)
    except ValueError:
        return None
    if not rel.parts:
        return None
    layer = rel.parts[0]
    return layer if layer in LAYER_RULES else None


def resolve_python_relative_layer(file_path: Path, spec: str) -> str | None:
    match = re.match(r"^(\.+)([A-Za-z0-9_\.]*)$", spec)
    if not match:
        return None

    dots = len(match.group(1))
    rest = match.group(2)

    module_path = file_path.relative_to(SRC_DIR).with_suffix("")
    package_parts = list(module_path.parts[:-1])

    up = dots - 1
    if up > len(package_parts):
        return None

    resolved_parts = package_parts[: len(package_parts) - up]
    if rest:
        resolved_parts.extend([part for part in rest.split(".") if part])

    if not resolved_parts:
        return None

    layer = resolved_parts[0]
    return layer if layer in LAYER_RULES else None


def resolve_import_layer(file_path: Path, spec: str) -> str | None:
    if spec.startswith("src."):
        parts = spec.split(".")
        if len(parts) > 1 and parts[1] in LAYER_RULES:
            return parts[1]

    if spec.startswith("src/"):
        parts = spec.split("/")
        if len(parts) > 1 and parts[1] in LAYER_RULES:
            return parts[1]

    if spec.startswith("@/"):
        parts = spec.split("/")
        if len(parts) > 1 and parts[1] in LAYER_RULES:
            return parts[1]

    if spec.startswith("."):
        if file_path.suffix == ".py":
            return resolve_python_relative_layer(file_path, spec)
        return resolve_relative_path_layer(file_path, spec)

    root_name = spec.split(".", 1)[0]
    if root_name in LAYER_RULES:
        return root_name

    return None


def check_dependencies() -> int:
    files = iter_source_files()
    violations: list[tuple[Path, int, str, str, str]] = []
    scanned = 0

    for file_path in files:
        source_layer = layer_from_path(file_path)
        if source_layer is None:
            continue

        scanned += 1
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        for lineno, spec in parse_import_specs(file_path, text):
            target_layer = resolve_import_layer(file_path, spec)
            if target_layer is None:
                continue
            if target_layer not in LAYER_RULES[source_layer]:
                violations.append((file_path, lineno, source_layer, spec, target_layer))

    if violations:
        print("Architecture dependency violations found:")
        for file_path, lineno, source_layer, spec, target_layer in violations:
            rel = file_path.relative_to(ROOT_DIR)
            print(
                f"- {rel}:{lineno} | {source_layer} -> {target_layer} not allowed "
                f"(import: {spec})"
            )
        return 1

    print(f"Architecture check passed ({scanned} files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(check_dependencies())
