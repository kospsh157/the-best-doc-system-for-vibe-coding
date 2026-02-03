# 개발 환경

## TL;DR (10줄 이내)
- 로컬 개발에 필요한 최소 정보를 기록한다.  

## 사용
- 레벨: L2 (작업 영역별)  
- 읽기: 개발 환경 설정/재현이 필요할 때.  
- 갱신: 언어/런타임/환경 변수/실행 방법이 바뀌었을 때.  
## 언어/런타임
- Python 3.10.13 (임베디드, scripts/python/ 폴더에 포함)
- 플랫폼: macOS (ARM64/Intel), Linux (x86_64), Windows (x86_64)

## 패키지 매니저
- 없음 (임베디드 Python 사용, 외부 의존성 없음)

## 필수 환경 변수
- 없음

## 로컬 실행 방법
- 문서 토큰 계산: `./scripts/run_doc_tokens.sh` (Unix/macOS) 또는 `scripts\run_doc_tokens.bat` (Windows) 또는 `python3 scripts/run_doc_tokens.py` (모든 플랫폼)  
