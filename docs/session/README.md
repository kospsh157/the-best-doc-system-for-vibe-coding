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
4) `docs/session/LOG.md` (최신 1~3개 항목)  
5) `docs/project/overview.md`  
6) `docs/project/scope.md`  
7) `docs/architecture/overview.md`  
8) `docs/architecture/structure.md`  
9) 필요 시 L1/L2/L3 문서  

## 세션 운영 프로토콜 (고정)
1) 복구: L0 읽기 + 최신 로그 1~3개 확인 + 현재 목표/다음 작업/리스크/구조 규칙 요약  
2) 실행: 명세 -> 구현 -> 아키텍처 검사 -> 테스트 -> 문서 갱신  
3) 인수인계: 상태/로그 갱신 + 변경 파일/테스트 결과/재개 포인트 기록 + 문서 품질 검사(`python3 scripts/check_docs.py`)  

## 사용자 문구 트리거
- 시작 문구 예시: `starter.md 읽고 문서 체계 이해한다음 프로젝트 구조 파악하고 할 작업 뭐가 있는지 파악해봐`
- 종료 문구 예시: `세션 종료할꺼야 문서 체계에 맞춰서 지금까지 한 작업들 문서 업데이트 해줘`
- 위 문구를 받으면 각 단계(복구/인수인계)를 생략 없이 수행한다.

## AI 빠른 복귀 체크 (60초)
1) 지금 목표 1줄 확인 (`현재 상태 > 현재 목표`)  
2) 다음 작업 Top 3 확인 (`현재 상태 > 다음 작업`)  
3) 최신 완료/미완료 확인 (`docs/session/LOG.md`)  
4) 블로커/리스크 확인 (`현재 상태 > 보류/리스크`)  
5) 구조 규칙 확인 (`docs/architecture/structure.md`)  
6) 토큰 상태 확인 (`python3 scripts/doc_token_guard.py`)  

## 문서 축약 안전장치 (필수)
- 에이전트는 비파괴 정리(중복 제거, 구조 개선, 링크 정리, 요약 보강)를 자동 수행한다.
- 토큰 과다 시에도 사용자 승인 전 문서 원문 삭제/축약 금지
- 30000 이상(WARN): 비파괴 간단 정리 자동 수행
- 40000 이상(EXCEEDED): 전체 문서 정밀 검토 후 삭제/축약 후보 제안, 사용자 승인 후 반영
- `프로젝트 기초`, `핵심 설계`, `지켜야 할 지침` 섹션은 삭제/축약하지 않는다.
- 축약 제안 시 반드시 포함:
1) 삭제/축약 후보
2) 유지할 핵심 정보
3) 예상 토큰 절감량
4) 승인 요청 문구
- 승인 후 적용 내역은 `docs/session/LOG.md`에 기록

## 프로젝트 스냅샷 (항상 최신)
- 각 항목은 1줄 요약으로 유지한다.
- 한 줄 요약: AI 세션 재개에 최적화된 Clean Architecture 기반 문서 시스템
- 핵심 도메인/용어: L0(필수)/L1(재개)/L2(작업별)/L3(심화) 문서 레벨, 세션 연속성
- 주요 기능/흐름: 세션 시작 시 L0 문서 읽기 → 구조/경계 검사 기반 작업 수행 → 문서 갱신 → 세션 종료
- 기술 스택/런타임: Python 3.10.13 임베디드(4개 플랫폼), Markdown 문서, Shell/Batch 스크립트
- 핵심 디렉터리/경로: docs/ (문서), src/ (클린아키텍처 레이어), tests/ (계층별 테스트), scripts/ (검사/실행 스크립트)
- 항상 알아야 할 것: 구조 변경 시 `docs/architecture/structure.md` 즉시 갱신, 구현 전후 `python3 scripts/check_arch.py` 실행, 종료 전 `python3 scripts/check_docs.py` 실행
- 중요 제약/가정: 문서는 docs/ 아래만, 계층 경계 준수, 구조 변경 시 문서 즉시 동기화
- 마지막 업데이트: 2026-02-28 17:50  

## 현재 상태 (항상 최신)
- 각 항목은 1줄 요약으로 유지한다.
- 현재 목표: 프로젝트 주제 확정 전에도 유지 가능한 클린아키텍처 시작 골격 고정
- 진행 중: 없음
- 다음 작업(Top 3): 1) 프로젝트 주제/도메인 확정, 2) 첫 기능 명세(`docs/specs/feature-*.md`) 작성, 3) 레이어별 첫 유스케이스 구현
- 보류/리스크: 프로젝트 주제 미정으로 도메인 모델/요구사항 문서가 비어 있음
- 주의사항: 프로젝트 주제 확정 전에는 구조/경계/품질 장치 변경만 수행하고 비즈니스 가정 구현은 보류
- 최근 변경 요약: 토큰 가드 임계치를 `경고 30000 / 예산 40000`으로 상향하고, 2단계 정리 정책(3만 간단정리/4만 정밀검토+승인삭제) 및 핵심 섹션 보호 규칙을 문서/스크립트에 반영
- 테스트/실행: `python3 scripts/check_arch.py` 통과, `python3 scripts/check_docs.py` 통과, `python3 scripts/doc_token_guard.py` 실행(OK, 12397 토큰)
- 중요한 경로: starter.md (토큰 관리+안전 축약 규칙), docs/{README.md,session/{README,LOG,END_PROMPT}.md,dev/{workflow,environment,testing}.md}, scripts/{check_arch.py,check_docs.py,doc_token_guard.py}, .githooks/pre-commit
- 마지막 업데이트: 2026-02-28 17:50  

## 주제 수령 시 즉시 실행 (필수)
1) `docs/project/overview.md`, `docs/project/scope.md`를 주제 기반으로 갱신
2) `docs/project/glossary.md`, `docs/project/roadmap.md`를 주제 기준으로 갱신
3) `docs/specs/feature-*.md` 첫 명세 작성 후 구현 시작
4) 필요 시 `docs/data/model.md`, `docs/integrations/external-services.md`, `docs/ops/runbook.md`를 함께 채움
5) 세션 종료 시 `docs/session/README.md`/`docs/session/LOG.md`를 반드시 동기화

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
- 재개 포인트: 다음 세션에서 바로 시작할 1개 작업을 명확히 작성  

## 세션 종료 체크리스트
1) 프로젝트 스냅샷/현재 상태 갱신(없으면 "없음")  
2) `docs/session/LOG.md`에 세션 로그 추가(최신 상단)  
3) 변경된 내용이 있으면 관련 문서 업데이트  
