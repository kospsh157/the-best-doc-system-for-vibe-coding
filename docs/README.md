# 문서 시스템 (AI 세션 친화)

이 저장소의 공식 문서는 `docs/` 아래에만 둔다. 문서의 목적은 세션 재시작 시에도 AI가 빠르고 정확하게 프로젝트를 이해하도록 돕는 것이다.

## 사용
- 레벨: L0 (항상 읽기)  
- 읽기: 세션 시작 시.  
- 갱신: 문서 체계/규칙/목록이 변경되었을 때.  
## 컨텍스트 사용 규칙
- L0: 항상 읽는 문서(필수)  
- L1: 작업 재개에 필요한 문서  
- L2: 작업 영역에만 필요한 문서(필요할 때만)  
- L3: 심화 참조/장문 문서(필요할 때만)  
- 모든 문서는 "사용" 섹션(레벨/읽기/갱신)을 가진다.  
- 각 문서는 "TL;DR(10줄 이내)"로 시작하고, 상세는 아래 섹션에 둔다.  
- 긴 로그/세부 내역은 L2 문서로 분리하고, L0/L1에는 요약만 둔다.  

## 읽기 순서 (세션 시작)
1) `starter.md`  
2) `docs/README.md`  
3) `docs/session/README.md`  
4) `docs/session/LOG.md` (최신 항목만)  
5) `docs/project/overview.md`  
6) `docs/project/scope.md`  
7) `docs/architecture/overview.md`  
8) `docs/architecture/structure.md`  
9) 필요 시 L1/L2/L3 문서  

## 문서 목록
### L0 (항상 읽기)
- `starter.md` : 세션 진입점  
- `docs/README.md` : 문서 체계 규칙(현재 문서)  
- `docs/session/README.md` : 프로젝트 스냅샷, 현재 상태, 세션 시작/종료  
- `docs/session/LOG.md` : 세션 로그(최신 항목만 읽기)  
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
