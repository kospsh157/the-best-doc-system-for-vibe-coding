# 프로젝트 세션 시작 안내

이 문서는 매 세션 시작 시 반드시 먼저 읽는다. 목적은 문서 체계를 이해하고, 프로젝트 구조를 빠르게 파악하며, 변경 사항을 문서에 정확히 반영하는 것이다.

## 사용
- 레벨: L0 (항상 읽기)  
- 읽기: 세션 시작 시.  
- 갱신: 문서 체계/세션 규칙/읽기 순서가 바뀌었을 때.  
## 프로젝트 이해 절차(에이전트)
1) `docs/README.md` 를 읽고 문서 구조와 규칙을 확인한다.  
2) `docs/session/README.md` 를 읽고 프로젝트 스냅샷/현재 상태를 파악한다.  
3) `docs/session/LOG.md` 의 최신 항목만 확인한다.  
4) `docs/project/overview.md` 를 읽고 프로젝트 목적/목표를 확인한다.  
5) `docs/project/scope.md` 를 읽고 범위/제약을 확인한다.  
6) `docs/architecture/overview.md` 를 읽고 Clean Architecture 기준을 확인한다.  
7) `docs/architecture/structure.md` 를 읽고 폴더 구조/경계를 확인한다.  
8) 필요 시 L1/L2 문서를 `docs/README.md` 안내에 따라 확인한다.  

## 문서 체계 규칙
- 문서는 `docs/` 아래에만 둔다.  
- 문서 분류를 위해 하위 폴더를 사용한다.  
- 변경 사항이 구조/규칙/동작에 영향을 주면 관련 문서를 업데이트한다.  
- 중요한 설계 결정은 `docs/architecture/decisions.md`에 기록한다.  
- 문서 간 링크는 상대 경로로 유지한다.  
- 상세 목록은 `docs/README.md` 참고.  
- 기본 원칙: L0는 항상 읽고, L1은 재개 맥락, L2는 작업 상세, L3는 심화 참조로 최소한만 읽는다.  

## AI 세션 프롬프트(필수)
이 문서를 읽은 뒤 아래 규칙을 반드시 따른다.
1) L0 8개 문서를 순서대로 읽고, 프로젝트 스냅샷/현재 상태/범위/구조를 짧게 이해한다.  
2) 불확실한 부분이 있을 때만 L1/L2/L3 문서를 추가로 읽는다.  
3) 세션 중 읽은 모든 문서를 기록한다(L0 포함).  
4) 작업 중 변경이 생기면 해당 문서를 즉시 갱신한다.  
5) 세션 종료 시 `docs/session/END_PROMPT.md`를 읽고 절차를 수행한다.  
6) 세션 시작 시 `python3 scripts/doc_tokens.py`로 문서 토큰 합계를 계산해 사용자에게 보고한다(현재 계산 방식은 추정치).  

## L0 고정 목록(항상 읽기)
1) `starter.md`  
2) `docs/README.md`  
3) `docs/session/README.md`  
4) `docs/session/LOG.md` (최신 항목만)  
5) `docs/project/overview.md`  
6) `docs/project/scope.md`  
7) `docs/architecture/overview.md`  
8) `docs/architecture/structure.md`  

## 작업 유형 판별 규칙(필수)
1) 작업 유형을 먼저 분류한다: 기능 추가/변경, 버그 수정, 리팩터링, 데이터 변경, 외부 연동, 테스트/품질, 배포/운영.  
2) 영향 레이어를 추정한다: Domain, Application, Interface, Infrastructure.  
3) L0로 충분하면 추가 문서를 읽지 않는다.  
4) L0로 부족하면 아래 매핑에 따라 문서를 선택한다.  

## 작업 유형 → 문서 매핑(필수)
- 기능 추가/변경: `docs/project/scope.md`, `docs/specs/README.md`, 관련 기능 스펙  
- 버그 수정: 관련 기능 스펙, 필요 시 `docs/architecture/structure.md`  
- 리팩터링/구조 변경: `docs/architecture/overview.md`, `docs/architecture/structure.md`, 필요 시 `docs/architecture/decisions.md`  
- 데이터 변경: `docs/data/model.md`, 필요 시 `docs/integrations/external-services.md`  
- 외부 연동: `docs/integrations/external-services.md`, 필요 시 `docs/architecture/decisions.md`  
- 테스트/품질: `docs/dev/testing.md`  
- 배포/운영: `docs/ops/runbook.md`  

## 문서 작성/갱신 트리거(필수)
- 기능 요구가 불명확하다 → `docs/specs/feature-이름.md` 신규 작성  
- 구조 변경이 발생했다 → `docs/architecture/structure.md` 갱신  
- 중요한 선택/트레이드오프가 발생했다 → `docs/architecture/decisions.md` 기록  
- 외부 계약/스펙이 변경되었다 → `docs/integrations/external-services.md` 갱신  
- 데이터 모델이 바뀌었다 → `docs/data/model.md` 갱신  

## 즉시 업데이트(작업 중 필수)
- `docs/session/README.md` : 목표/다음 작업/리스크가 바뀔 때  
- `docs/architecture/decisions.md` : 되돌리기 어려운 결정이 생길 때  
- `docs/architecture/structure.md` : 구조/경계가 바뀔 때  
- `docs/project/scope.md` : 범위/제약이 바뀔 때  
- `docs/data/model.md` 또는 `docs/integrations/external-services.md` : 데이터/계약 변경 시  

## 세션 말 업데이트(종료 시)
- `docs/session/LOG.md` : 세션 요약 + 참조 문서 기록  
- `docs/specs/feature-*.md` : 기능 요구 확정/변경 시  
- `docs/dev/testing.md` : 테스트 전략/명령 변경 시  
- `docs/dev/environment.md` : 개발 환경/실행 방법 변경 시  
- `docs/ops/runbook.md` : 배포/운영 절차 변경 시  

## 세션 연속성 규칙
- 프로젝트 스냅샷/현재 상태는 `docs/session/README.md`가 기준이다.  
- 세션 로그는 `docs/session/LOG.md`가 기준이다.  
- 세션 시작 전에 상태를 확인하고, 종료 전에 반드시 갱신한다(없으면 "없음" 명시).  
- 세션 로그는 최신 항목을 상단에 둔다.  
- 세션 종료 시에는 사용자 요청 유무와 관계없이 `docs/session/END_PROMPT.md`를 읽고 그대로 수행한다.  

## 세션 문서 사용법(필수)
- 시작: `docs/session/README.md`를 읽고 절차를 따른다.  
- 현재 상태: 작업 시작 전 확인하고, 종료 전에 반드시 최신화한다.  
- 히스토리: 세션 종료 시 `docs/session/LOG.md`에 로그를 추가한다(최신 항목 상단).  

## Clean Architecture 기본 원칙
- 의존성은 항상 안쪽(도메인)으로만 향한다.  
- 도메인 규칙은 프레임워크/DB/외부 API에 의존하지 않는다.  
- 인터페이스(입력/출력)는 도메인/애플리케이션을 침범하지 않는다.  

## 기본 프로젝트 구조(초기 제안)
- `src/domain/` : 엔티티, 값 객체, 도메인 서비스  
- `src/application/` : 유스케이스, 애플리케이션 서비스  
- `src/interface/` : 컨트롤러, 프레젠터, DTO  
- `src/infrastructure/` : DB, 외부 API, 메시징 등 구현  
- `src/entrypoints/` : CLI/HTTP 등 진입 지점  
- `tests/` : 테스트  
- `docs/` : 문서  

## 문서 업데이트 규칙
- 구조/경계 변경: `docs/architecture/overview.md`, `docs/architecture/structure.md` 갱신  
- 요구사항/명세 변경: `docs/project/scope.md`, `docs/specs/` 갱신  
- 의사결정: `docs/architecture/decisions.md` 기록  
- 개발/운영 변경: `docs/dev/`, `docs/ops/` 갱신  
- 데이터/연동 변경: `docs/data/`, `docs/integrations/` 갱신  

## 세션 종료 체크리스트
1) `docs/session/README.md`와 `docs/session/LOG.md`를 갱신한다.  
2) 변경된 내용이 있으면 관련 문서를 업데이트한다.  
3) `docs/session/END_PROMPT.md`의 절차를 따른다.  
