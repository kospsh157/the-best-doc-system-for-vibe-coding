#!/bin/bash
# OS별 임베디드 Python 자동 선택 및 실행

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BASE="$SCRIPT_DIR/python"

# OS 및 아키텍처 감지
detect_platform() {
    local os=$(uname -s)
    local arch=$(uname -m)

    case "$os" in
        Darwin)
            case "$arch" in
                arm64|aarch64)
                    echo "darwin-arm64"
                    ;;
                x86_64)
                    echo "darwin-x86_64"
                    ;;
                *)
                    echo "Unsupported macOS architecture: $arch" >&2
                    exit 1
                    ;;
            esac
            ;;
        Linux)
            case "$arch" in
                x86_64)
                    echo "linux-x86_64"
                    ;;
                *)
                    echo "Unsupported Linux architecture: $arch" >&2
                    exit 1
                    ;;
            esac
            ;;
        MINGW*|MSYS*|CYGWIN*)
            echo "windows-x86_64"
            ;;
        *)
            echo "Unsupported OS: $os" >&2
            exit 1
            ;;
    esac
}

PLATFORM=$(detect_platform)
PYTHON_BIN="$PYTHON_BASE/$PLATFORM/python/bin/python3"

if [ ! -f "$PYTHON_BIN" ]; then
    echo "Error: Python binary not found at $PYTHON_BIN" >&2
    exit 1
fi

# doc_tokens.py 실행
exec "$PYTHON_BIN" "$SCRIPT_DIR/doc_tokens.py" "$@"
