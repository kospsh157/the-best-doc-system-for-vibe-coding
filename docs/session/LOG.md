# 세션 로그

## 사용
- 레벨: L0 (항상 읽기, 최신 1~3개)  
- 읽기: 세션 시작 시 최신 1~3개 항목 확인.  
- 갱신: 세션 종료 시 새 항목 추가.  
## 사용 규칙
- 최신 항목을 상단에 둔다.  
- 각 항목은 8줄 이내 요약으로 작성한다(`재개 포인트` 포함).  
- 참조는 세션 중 실제로 읽은 모든 문서를 기록한다(L0 포함).  

## 항목 템플릿
- 목표:
- 변경:
- 파일:
- 참조:
- 결정:
- 테스트:
- 다음:
- 재개 포인트:

## 2026-02-28 17:45
- 목표: 토큰 운영 기준을 경고 3만/예산 4만으로 조정하고 정리 정책을 단계화
- 변경: 토큰 가드 기본값을 40000/0.75로 상향, 3만 간단정리/4만 정밀검토+승인삭제 규칙 반영, 핵심 섹션(프로젝트 기초/핵심 설계/지침) 보호 규칙 명시
- 파일: scripts/doc_token_guard.py, starter.md, docs/{README.md,session/{README,LOG,END_PROMPT}.md,dev/{workflow,environment}.md,architecture/decisions.md}
- 참조: scripts/doc_token_guard.py, starter.md, docs/{README.md,session/{README,LOG,END_PROMPT}.md,dev/{workflow,environment}.md,architecture/decisions.md}
- 결정: 성장 단계 프로젝트 기본 토큰 운영값은 경고 30000/예산 40000으로 유지
- 테스트: `python3 scripts/check_arch.py` 통과, `python3 scripts/check_docs.py` 통과, `python3 scripts/doc_token_guard.py` 실행(OK, 12397), `./scripts/run_doc_tokens.sh` 실행(12397 토큰)
- 다음: 토큰이 30000에 접근하면 비파괴 정리 먼저 수행, 40000 도달 시 삭제 후보 승인 요청 절차 적용
- 재개 포인트: 정리 필요 시 우선 top_files 기준으로 비파괴 정리 후보부터 제시

## 2026-02-28 17:30
- 목표: 프로젝트 성장 구간을 고려해 토큰 가드 기준 상향
- 변경: `scripts/doc_token_guard.py` 기본 예산/경고비율을 30000/0.75로 조정하고, 환경 변수 조정 방법을 starter/README/environment에 반영
- 파일: scripts/doc_token_guard.py, starter.md, docs/{README.md,dev/environment.md,session/{README,LOG}.md}
- 참조: scripts/doc_token_guard.py, starter.md, docs/README.md, docs/dev/environment.md, docs/session/{README,LOG}.md
- 결정: 초기 문서 체계 확장 단계에서는 12000 기준이 과도하게 보수적이므로 성장형 가드를 기본값으로 사용
- 테스트: `python3 scripts/check_arch.py` 통과, `python3 scripts/check_docs.py` 통과, `python3 scripts/doc_token_guard.py` 실행(OK, 11640), `./scripts/run_doc_tokens.sh` 실행(11640 토큰)
- 다음: 프로젝트 주제 확정 후 문서 증가 추이에 따라 예산을 다시 미세 조정
- 재개 포인트: 필요 시 `DOC_TOKEN_BUDGET`, `DOC_TOKEN_WARN_RATIO` 값만 조정해 프로젝트 단계별 운영

## 2026-02-28 17:20
- 목표: 토큰 과다 상황에서 자동 정리와 삭제 승인 규칙을 명확히 구분
- 변경: 비파괴 정리 자동 수행 허용, 원문 삭제/축약은 사용자 승인 필수 규칙을 starter/README/session/END_PROMPT에 명시
- 파일: starter.md, docs/{README.md,session/{README,END_PROMPT}.md}
- 참조: starter.md, docs/README.md, docs/session/{README,END_PROMPT}.md
- 결정: 에이전트는 자동 정리를 적극 수행하되 삭제/절단은 승인 기반으로만 수행
- 테스트: `python3 scripts/check_arch.py` 통과, `python3 scripts/check_docs.py` 통과, `python3 scripts/doc_token_guard.py` 실행(WARN, 11300)
- 다음: 토큰 과다 시 축약 후보/영향/절감량/승인 요청 템플릿으로 먼저 제안
- 재개 포인트: 필요 시 현재 상위 토큰 파일(starter/session/README)에 대해 비파괴 정리 후보부터 제시

## 2026-02-28 17:05
- 목표: 토큰 과다 시 문서 축약 안전장치를 강제해 필요한 내용 삭제를 방지
- 변경: `starter.md`/`docs/README.md`/`docs/session/README.md`에 토큰 관리 및 사용자 승인 규칙 추가, 종료 프롬프트/워크플로우에 승인 단계 반영, `scripts/doc_token_guard.py` 추가
- 파일: starter.md, docs/{README.md,session/{README,LOG,END_PROMPT}.md,dev/{workflow,environment,testing}.md}, scripts/doc_token_guard.py, scripts/check_docs.py, .githooks/pre-commit, scripts/install_git_hook.sh, .gitignore
- 참조: starter.md, docs/README.md, docs/session/{README,LOG,END_PROMPT}.md, docs/dev/{workflow,environment,testing}.md, scripts/doc_tokens.py
- 결정: 토큰 과다(WARN/EXCEEDED) 상태에서 사용자 승인 없는 문서 원문 삭제/축약 금지
- 테스트: `python3 scripts/check_arch.py` 통과, `python3 scripts/check_docs.py` 통과, `python3 scripts/doc_token_guard.py` 실행(WARN, 11022), `./scripts/run_doc_tokens.sh` 실행(11022 토큰)
- 다음: 주제 수령 전까지는 축약 후보 제안만 수행하고, 실제 삭제/축약은 승인 후에만 진행
- 재개 포인트: 토큰 축약이 필요하면 후보/영향/절감량을 먼저 제시하고 사용자 승인 요청

## 2026-02-28 16:45
- 목표: 문서 품질을 프로젝트 진행 품질 게이트로 강제
- 변경: 문서 중복/누락/플레이스홀더 방지 규칙 추가, `scripts/check_docs.py` 신규 작성, pre-commit 훅에 문서 검사 연동, 종료 프롬프트에 문서 검사 단계 추가
- 파일: starter.md, docs/{README.md,session/{README,LOG,END_PROMPT}.md,dev/{environment,workflow,testing}.md,architecture/decisions.md}, scripts/{check_docs.py,install_git_hook.sh}, .githooks/pre-commit
- 참조: starter.md, docs/README.md, docs/session/{README,LOG,END_PROMPT}.md, docs/dev/{environment,workflow,testing}.md, docs/architecture/decisions.md
- 결정: 문서 업데이트 완료 조건에 `python3 scripts/check_docs.py` 통과를 포함
- 테스트: `python3 scripts/check_arch.py` 통과, `python3 scripts/check_docs.py` 통과, `./scripts/run_doc_tokens.sh` 실행(10251 토큰)
- 다음: 프로젝트 주제 수령 후 첫 기능 명세를 작성하고 문서 품질 게이트를 동일하게 적용
- 재개 포인트: 주제 수령 직후 `docs/project/*`와 `docs/specs/feature-*.md`를 주제 기반으로 채운다

## 2026-02-28 16:30
- 목표: 사용자 시작/종료 문구 기반 고정 프로토콜 반영 및 문서 품질 이슈 정리
- 변경: 3단계 운영 프로토콜(복구/실행/인수인계) 고정, 로그 포맷/읽기 범위 규칙 정합화, 공란 문서 `미정/없음` 처리, pre-commit 훅 자동화 추가
- 파일: starter.md, docs/{README.md,session/{README,LOG,END_PROMPT}.md,dev/{environment,workflow,testing}.md,data/model.md,integrations/external-services.md,ops/runbook.md,specs/README.md}, scripts/install_git_hook.sh, .githooks/pre-commit
- 참조: starter.md, docs/README.md, docs/session/{README,LOG,END_PROMPT}.md, docs/dev/{environment,workflow,testing}.md, docs/data/model.md, docs/integrations/external-services.md, docs/ops/runbook.md, docs/specs/README.md
- 결정: 세션 시작/종료 문구가 오면 프로토콜 단계를 생략 없이 수행
- 테스트: `python3 scripts/check_arch.py` 통과, `./scripts/run_doc_tokens.sh` 실행(8984 토큰), `./scripts/install_git_hook.sh` 실행 성공
- 다음: 프로젝트 주제 확정 후 첫 기능 명세(`docs/specs/feature-*.md`) 작성
- 재개 포인트: 주제 확정 직후 `docs/specs/feature-<name>.md`를 만들고 현재 상태/재개 포인트를 채운다

## 2026-02-28 16:00
- 목표: AI 에이전트 세션 복귀 중심으로 문서 체계를 강화
- 변경: starter/README/session 문서에 "주제 미정 단계 운영 규칙"과 "빠른 복귀 체크" 추가, 구조 강제 장치(check_arch) 반영
- 파일: starter.md, docs/README.md, docs/session/{README,LOG}.md, docs/project/{overview,scope,roadmap,glossary}.md, docs/architecture/{structure,decisions}.md, docs/dev/{environment,workflow,testing}.md, docs/specs/{README,TEMPLATE}.md, scripts/check_arch.py, src/**, tests/**
- 참조: starter.md, docs/README.md, docs/session/README.md, docs/session/LOG.md, docs/project/overview.md, docs/project/scope.md, docs/project/roadmap.md, docs/architecture/overview.md, docs/architecture/structure.md, docs/specs/README.md, docs/specs/TEMPLATE.md
- 결정: 프로젝트 주제 확정 전에는 비즈니스 구현보다 구조/경계/검사 자동화를 우선
- 테스트: `python3 scripts/check_arch.py` 통과, `./scripts/run_doc_tokens.sh` 실행(8101 토큰)
- 다음: 프로젝트 주제/도메인 확정 후 첫 기능 명세(`docs/specs/feature-*.md`) 작성
- 재개 포인트: 프로젝트 주제 확정 후 `docs/specs/feature-*.md` 1개를 먼저 작성

## 2026-02-03 17:00
- 목표: 사용자 환경 독립적인 문서 토큰 계산 시스템 구축
- 변경: 임베디드 Python 4개 플랫폼 설정(305MB), doc_tokens.py 알고리즘 개선(CJK 처리), OS 자동 감지 실행 스크립트 3종 작성
- 파일: scripts/python/ (신규), scripts/doc_tokens.py (수정), scripts/run_doc_tokens.{sh,bat,py} (신규), docs/session/README.md (갱신)
- 참조: starter.md, docs/README.md, docs/session/README.md, docs/session/LOG.md, docs/session/END_PROMPT.md, docs/project/overview.md, docs/project/scope.md, docs/architecture/overview.md, docs/architecture/structure.md
- 결정: Python 3.10.13 임베디드 사용, 플랫폼별 Python 번들(305MB), 개선 토큰 추정(영문 4자/토큰, 한글 1.7자/토큰, CJK 1.7자/토큰)
- 테스트: macOS ARM64에서 실행 확인, 총 4975 토큰 계산 성공
- 다음: Windows/Linux 환경 실제 테스트, 프로젝트 실제 기능 명세 작성  
- 재개 포인트: Windows/Linux 환경에서 토큰 계산 스크립트 실제 실행 검증
