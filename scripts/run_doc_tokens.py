#!/usr/bin/env python3
"""
범용 OS 감지 및 임베디드 Python 실행 래퍼
모든 플랫폼(Windows, macOS, Linux)에서 작동
"""
import os
import sys
import platform
import subprocess
from pathlib import Path


def detect_platform():
    """현재 OS와 아키텍처를 감지하여 플랫폼 식별자 반환"""
    system = platform.system()
    machine = platform.machine()

    if system == "Darwin":  # macOS
        if machine in ("arm64", "aarch64"):
            return "darwin-arm64"
        elif machine == "x86_64":
            return "darwin-x86_64"
        else:
            raise RuntimeError(f"Unsupported macOS architecture: {machine}")

    elif system == "Linux":
        if machine == "x86_64":
            return "linux-x86_64"
        else:
            raise RuntimeError(f"Unsupported Linux architecture: {machine}")

    elif system == "Windows":
        return "windows-x86_64"

    else:
        raise RuntimeError(f"Unsupported OS: {system}")


def main():
    script_dir = Path(__file__).parent.resolve()
    python_base = script_dir / "python"

    # 플랫폼 감지
    try:
        platform_id = detect_platform()
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Python 바이너리 경로 설정
    if platform.system() == "Windows":
        python_bin = python_base / platform_id / "python" / "python.exe"
    else:
        python_bin = python_base / platform_id / "python" / "bin" / "python3"

    if not python_bin.exists():
        print(f"Error: Python binary not found at {python_bin}", file=sys.stderr)
        return 1

    # doc_tokens.py 실행
    doc_tokens_script = script_dir / "doc_tokens.py"
    cmd = [str(python_bin), str(doc_tokens_script)] + sys.argv[1:]

    try:
        result = subprocess.run(cmd)
        return result.returncode
    except Exception as e:
        print(f"Error executing Python: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
