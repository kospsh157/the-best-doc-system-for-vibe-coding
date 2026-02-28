# 문서 시스템 (AI 세션 친화)

이 저장소의 공식 문서는 `docs/` 아래에만 둔다. 문서의 목적은 세션 재시작 시에도 AI가 빠르고 정확하게 프로젝트를 이해하도록 돕는 것이다.

## 사용
- 레벨: L0 (항상 읽기)  
- 읽기: 세션 시작 시.  
- 갱신: 문서 체계/규칙/목록이 변경되었을 때.  

## 주 목적 (필수)
- 1순위: AI 에이전트가 세션 시작 직후 프로젝트를 빠르게 복구(컨텍스트 복원)하도록 돕는다.
- 2순위: 개발자가 동일한 문서를 참고해 현재 상태를 확인할 수 있게 한다.
- 문서는 "빠른 복귀"와 "필요 시 상세 참조"를 동시에 지원해야 한다.

## AI 복귀 정보 맵 (필수)
- 프로젝트의 한 줄 요약/현재 목표: `docs/session/README.md`
- 지난 세션의 실제 작업/결정/테스트: `docs/session/LOG.md` (최신 상단)
- 프로젝트 목적/비목표: `docs/project/overview.md`
- 범위/제약/주의사항: `docs/project/scope.md`
- 구조/경계/의존성 규칙: `docs/architecture/structure.md`
- 핵심 설계 판단 근거: `docs/architecture/decisions.md`
- 다음에 구현할 기능 상세: `docs/specs/feature-*.md`

## 컨텍스트 사용 규칙
- L0: 항상 읽는 문서(필수)  
- L1: 작업 재개에 필요한 문서  
- L2: 작업 영역에만 필요한 문서(필요할 때만)  
- L3: 심화 참조/장문 문서(필요할 때만)  
- 모든 문서는 "사용" 섹션(레벨/읽기/갱신)을 가진다.  
- 각 문서는 "TL;DR(10줄 이내)"로 시작하고, 상세는 아래 섹션에 둔다.  
- 긴 로그/세부 내역은 L2 문서로 분리하고, L0/L1에는 요약만 둔다.  
- 세션 시작 60초 안에 "현재 목표/다음 작업/리스크"를 찾을 수 있어야 한다.
- 문서에 "미정"이 있으면 그대로 명시하고, 추측으로 채우지 않는다.

## 문서 품질 원칙 (필수)
- 중복 금지: 같은 사실/결정/규칙은 단일 기준 문서 1곳에만 기록하고, 다른 문서는 링크/요약만 둔다.
- 누락 금지: 변경 사항이 발생하면 영향 문서를 동시에 갱신한다.
- 단일 출처(SSOT):
  - 현재 상태/다음 작업/리스크: `docs/session/README.md`
  - 세션 히스토리: `docs/session/LOG.md`
  - 구조/의존성 규칙: `docs/architecture/structure.md`
  - 범위/제약: `docs/project/scope.md`
  - 설계 결정: `docs/architecture/decisions.md`
  - 기능 상세 요구사항: `docs/specs/feature-*.md`
- 문서 품질 검사 명령: `python3 scripts/check_docs.py`

## 토큰 예산 운영 원칙 (필수)
- 토큰 확인은 세션 시작/종료 시 수행한다: `python3 scripts/doc_tokens.py`
- 권장 가드 명령: `python3 scripts/doc_token_guard.py`
- 기본 가드값: 예산 40000, 경고 30000(비율 0.75, 프로젝트 성장 고려)
- 프로젝트별 조정: `DOC_TOKEN_BUDGET`, `DOC_TOKEN_WARN_RATIO` 환경 변수 사용
- 토큰 과다 시 우선순위:
1) 중복 제거(원문 삭제 없이 링크/요약화)
2) 장문 로그 분리(L2/L3로 이동)
3) 사용자 승인 후에만 원문 축약/삭제
- 30000 이상(WARN): 비파괴 간단 정리 자동 수행
- 40000 이상(EXCEEDED): 전체 문서 정밀 검토 + 삭제/축약 후보 제안 + 사용자 승인 후 반영
- 에이전트는 비파괴 정리(중복 정리, 링크화, 재구성, 요약 섹션 추가)를 선제적으로 수행한다.
- 에이전트는 사용자 명시 승인 없이 문서 내용을 삭제하지 않는다.
- `프로젝트 기초`, `핵심 설계`, `지켜야 할 지침` 섹션은 축약/삭제 대상에서 제외한다.

## 읽기 순서 (세션 시작)
1) `starter.md`  
2) `docs/README.md`  
3) `docs/session/README.md`  
4) `docs/session/LOG.md` (최신 1~3개 항목)  
5) `docs/project/overview.md`  
6) `docs/project/scope.md`  
7) `docs/architecture/overview.md`  
8) `docs/architecture/structure.md`  
9) 필요 시 L1/L2/L3 문서  

## 세션 시작 체크 (AI용)
1) 현재 목표 1줄 확인 (`docs/session/README.md`)  
2) 다음 작업 Top 3 확인 (`docs/session/README.md`)  
3) 최신 변경/결정/테스트 확인 (`docs/session/LOG.md`)  
4) 제약/금지사항 확인 (`docs/project/scope.md`)  
5) 구조/의존성 규칙 확인 (`docs/architecture/structure.md`)  

## 주제 확정 후 문서 운영 (필수)
- 문서 체계(L0/L1/L2/L3, 읽기 순서, 계층 규칙)는 유지하고 문서 내용만 프로젝트 주제로 채운다.
- 에이전트는 주제 수령 후 아래 순서로 문서를 갱신한다.
1) `docs/project/overview.md`, `docs/project/scope.md`
2) `docs/project/glossary.md`, `docs/project/roadmap.md`
3) `docs/specs/feature-*.md`(첫 기능 명세)
4) 필요 시 `docs/data/model.md`, `docs/integrations/external-services.md`, `docs/ops/runbook.md`
- 이후 구현/수정/리팩터링 시에도 같은 문서 체계를 유지하며 세션 문서를 계속 동기화한다.

## 문서 목록
### L0 (항상 읽기)
- `starter.md` : 세션 진입점  
- `docs/README.md` : 문서 체계 규칙(현재 문서)  
- `docs/session/README.md` : 프로젝트 스냅샷, 현재 상태, 세션 시작/종료  
- `docs/session/LOG.md` : 세션 로그(최신 1~3개 읽기)  
- `docs/project/overview.md` : 프로젝트 요약/목표  
- `docs/project/scope.md` : 범위/비범위/제약  
- `docs/architecture/overview.md` : Clean Architecture 원칙  
- `docs/architecture/structure.md` : 폴더 구조/경계  

### 세션 도구
- `docs/session/END_PROMPT.md` : 세션 종료용 사용자 프롬프트  

### L1 (작업 재개 시)
- `docs/project/glossary.md` : 도메인 용어  
- `docs/project/roadmap.md` : 마일스톤/우선순위  
- `docs/architecture/decisions.md` : 의사결정 로그  

### L2 (작업 영역별)
- `docs/architecture/adr/0000-template.md` : ADR 템플릿  
- `docs/specs/README.md` : 기능 명세 인덱스  
- `docs/specs/TEMPLATE.md` : 기능 명세 템플릿  
- `docs/dev/environment.md` : 개발 환경  
- `docs/dev/workflow.md` : 개발 워크플로우  
- `docs/dev/testing.md` : 테스트 전략  
- `docs/ops/runbook.md` : 운영/배포  
- `docs/data/model.md` : 데이터 모델  
- `docs/integrations/external-services.md` : 외부 연동  

### L3 (심화 참조)
- 장문 설계서/외부 스펙/아카이브 문서(필요 시 추가)  

## L2 읽기 트리거
- 기능 구현: `docs/specs/`  
- 명세 작성/수정: `docs/specs/README.md`, `docs/specs/TEMPLATE.md`  
- 테스트/품질: `docs/dev/testing.md`  
- 배포/운영: `docs/ops/runbook.md`  
- 데이터/연동: `docs/data/model.md`, `docs/integrations/external-services.md`  

## L3 읽기 트리거
- 외부 계약/스펙 확인이 필요한 경우  
- 장문 설계 검토가 필요한 경우  

## 업데이트 규칙
- 프로젝트 스냅샷/상태: `docs/session/README.md`  
- 요구사항/범위: `docs/project/scope.md`  
- 구조/경계: `docs/architecture/overview.md`, `docs/architecture/structure.md`  
- 의사결정: `docs/architecture/decisions.md`  
- 기능 명세: `docs/specs/`  
- 개발/운영: `docs/dev/`, `docs/ops/`  
- 데이터/연동: `docs/data/`, `docs/integrations/`  
