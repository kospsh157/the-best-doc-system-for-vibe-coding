@echo off
REM OS별 임베디드 Python 자동 선택 및 실행 (Windows)

setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "PYTHON_BASE=%SCRIPT_DIR%python"

REM Windows는 항상 x86_64
set "PLATFORM=windows-x86_64"
set "PYTHON_BIN=%PYTHON_BASE%\%PLATFORM%\python\python.exe"

if not exist "%PYTHON_BIN%" (
    echo Error: Python binary not found at %PYTHON_BIN% 1>&2
    exit /b 1
)

REM doc_tokens.py 실행
"%PYTHON_BIN%" "%SCRIPT_DIR%doc_tokens.py" %*
