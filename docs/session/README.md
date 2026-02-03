# 세션 운영

## TL;DR (10줄 이내)
- 이 문서는 프로젝트 스냅샷과 현재 상태의 단일 기준이다.  
- 세션 시작 시 읽고, 종료 전에 반드시 갱신한다.  
- 세션 로그는 `docs/session/LOG.md`에만 기록한다.  
- 세션 종료 시 `docs/session/END_PROMPT.md`를 사용한다.  

## 사용
- 레벨: L0 (항상 읽기)  
- 읽기: 세션 시작 시.  
- 갱신: 세션 종료 시 또는 프로젝트 스냅샷/현재 상태가 변경되었을 때.  
## 세션 시작
1) `starter.md`  
2) `docs/README.md`  
3) `docs/session/README.md` (프로젝트 스냅샷/현재 상태)  
4) `docs/session/LOG.md` (최신 항목만)  
5) `docs/project/overview.md`  
6) `docs/project/scope.md`  
7) `docs/architecture/overview.md`  
8) `docs/architecture/structure.md`  
9) 필요 시 L1/L2/L3 문서  

## 프로젝트 스냅샷 (항상 최신)
- 각 항목은 1줄 요약으로 유지한다.
- 한 줄 요약: AI 세션 재개에 최적화된 Clean Architecture 기반 문서 시스템
- 핵심 도메인/용어: L0(필수)/L1(재개)/L2(작업별)/L3(심화) 문서 레벨, 세션 연속성
- 주요 기능/흐름: 세션 시작 시 L0 문서 읽기 → 작업 수행 → 문서 갱신 → 세션 종료
- 기술 스택/런타임: Python 3.10.13 임베디드(4개 플랫폼), Markdown 문서, Shell/Batch 스크립트
- 핵심 디렉터리/경로: docs/ (문서), scripts/python/ (임베디드 Python), scripts/run_doc_tokens.* (실행 스크립트)
- 중요 제약/가정: 문서는 docs/ 아래만, 토큰 효율 우선, Clean Architecture 준수
- 마지막 업데이트: 2026-02-03 17:00  

## 현재 상태 (항상 최신)
- 각 항목은 1줄 요약으로 유지한다.
- 현재 목표: 사용자 환경 독립적인 토큰 계산 시스템 구축 완료
- 진행 중: 없음
- 다음 작업(Top 3): 1) 다른 플랫폼에서 실행 테스트, 2) 프로젝트 실제 기능 정의, 3) 아키텍처 구조 구현
- 보류/리스크: Windows/Linux 환경 실제 테스트 미완료(macOS ARM64만 확인)
- 최근 변경 요약: 임베디드 Python 4개 플랫폼 설정(305MB), 토큰 추정 알고리즘 개선(영문 4자/토큰, 한글 1.7자/토큰), OS 자동 감지 실행 스크립트 3종 작성
- 테스트/실행: `./scripts/run_doc_tokens.sh` 또는 `python3 scripts/run_doc_tokens.py` (4975 토큰 계산 확인)
- 중요한 경로: scripts/python/ (임베디드 Python), scripts/doc_tokens.py (알고리즘), scripts/run_doc_tokens.* (실행)
- 마지막 업데이트: 2026-02-03 17:00  

## 세션 로그 (최신 상단)
- 참조에는 세션 중 읽은 모든 문서를 기록한다(L0 포함).  
### YYYY-MM-DD HH:MM
- 목표:  
- 변경:  
- 파일:  
- 참조:  
- 결정:  
- 테스트:  
- 다음:  

## 세션 종료 체크리스트
1) 프로젝트 스냅샷/현재 상태 갱신(없으면 "없음")  
2) `docs/session/LOG.md`에 세션 로그 추가(최신 상단)  
3) 변경된 내용이 있으면 관련 문서 업데이트  
