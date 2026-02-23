#!/usr/bin/env python3
from pathlib import Path


def iter_files():
    yield Path("starter.md")
    for path in sorted(Path("docs").rglob("*.md")):
        yield path


def approx_tokens(text):
    """
    Improved token estimation for multilingual text.

    Rules:
    - ASCII (English): ~4 chars per token
    - CJK characters (Korean, Chinese, Japanese): ~1.5-2 chars per token
    - Whitespace and punctuation contribute to tokens
    """
    if not text:
        return 0

    # Count different character types
    ascii_alphanumeric = 0
    cjk_chars = 0
    other_chars = 0

    for ch in text:
        code = ord(ch)

        # CJK Unified Ideographs and extensions
        # Korean: 0xAC00-0xD7AF (Hangul Syllables)
        # Chinese/Japanese: 0x4E00-0x9FFF (CJK Unified Ideographs)
        if (0xAC00 <= code <= 0xD7AF or  # Korean Hangul
            0x4E00 <= code <= 0x9FFF or  # CJK Ideographs
            0x3040 <= code <= 0x309F or  # Hiragana
            0x30A0 <= code <= 0x30FF):   # Katakana
            cjk_chars += 1
        elif code < 128:  # ASCII
            ascii_alphanumeric += 1
        else:  # Other Unicode
            other_chars += 1

    # Token estimation
    # - ASCII: ~4 chars per token (English words average ~4-5 chars)
    # - CJK: ~1.7 chars per token (empirically more accurate)
    # - Other: ~2.5 chars per token
    tokens = (
        ascii_alphanumeric / 4.0 +
        cjk_chars / 1.7 +
        other_chars / 2.5
    )

    return int(tokens + 0.5)  # Round to nearest integer


def main():
    files = list(iter_files())
    total = 0
    per_file = []
    tokenizer = "approx"

    for path in files:
        text = path.read_text()
        tokens = approx_tokens(text)
        total += tokens
        per_file.append((path, tokens))

    print(f"tokenizer: {tokenizer}")
    print(f"total_tokens: {total}")
    for path, tokens in per_file:
        print(f"{path}: {tokens}")


if __name__ == "__main__":
    raise SystemExit(main())
