#!/usr/bin/env python3
from pathlib import Path
import argparse
import subprocess
import sys


def iter_files():
    yield Path("starter.md")
    for path in sorted(Path("docs").rglob("*.md")):
        yield path


def approx_tokens(text):
    ascii_chars = sum(1 for ch in text if ord(ch) < 128)
    non_ascii = len(text) - ascii_chars
    return int(ascii_chars / 4 + non_ascii)


def try_import_tiktoken():
    try:
        import tiktoken  # type: ignore
    except Exception:
        return None
    return tiktoken


def install_tiktoken():
    cmd = [sys.executable, "-m", "pip", "install", "tiktoken"]
    subprocess.check_call(cmd)


def parse_args():
    parser = argparse.ArgumentParser(description="Estimate token counts for docs.")
    parser.add_argument(
        "--auto-install",
        action="store_true",
        help="Install tiktoken with pip if missing.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Confirm auto-install without an interactive prompt.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    files = list(iter_files())
    total = 0
    per_file = []
    tokenizer = "approx"
    exact = False
    tiktoken = try_import_tiktoken()

    if tiktoken is None and args.auto_install:
        if not args.yes:
            print(
                "auto-install requested but --yes not set; aborting.",
                file=sys.stderr,
            )
            print(
                "re-run with: python3 scripts/doc_tokens.py --auto-install --yes",
                file=sys.stderr,
            )
            return 2
        print("installing tiktoken via pip (requires network access)...", file=sys.stderr)
        try:
            install_tiktoken()
        except Exception as exc:
            print(f"install failed: {exc}", file=sys.stderr)
            return 1
        tiktoken = try_import_tiktoken()

    if tiktoken is not None:
        enc = tiktoken.get_encoding("cl100k_base")
        tokenizer = "tiktoken:cl100k_base"
        exact = True
        for path in files:
            text = path.read_text()
            tokens = len(enc.encode(text))
            total += tokens
            per_file.append((path, tokens))
    else:
        for path in files:
            text = path.read_text()
            tokens = approx_tokens(text)
            total += tokens
            per_file.append((path, tokens))

    print(f"tokenizer: {tokenizer}")
    print(f"total_tokens: {total}")
    for path, tokens in per_file:
        print(f"{path}: {tokens}")
    if not exact:
        print(
            "note: approximate; install tiktoken for exact counts",
            file=sys.stderr,
        )
        print(
            "note: run with --auto-install --yes after user approval",
            file=sys.stderr,
        )


if __name__ == "__main__":
    raise SystemExit(main())
