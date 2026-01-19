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
- 한 줄 요약:  
- 핵심 도메인/용어:  
- 주요 기능/흐름:  
- 기술 스택/런타임:  
- 핵심 디렉터리/경로:  
- 중요 제약/가정:  
- 마지막 업데이트: YYYY-MM-DD HH:MM  

## 현재 상태 (항상 최신)
- 각 항목은 1줄 요약으로 유지한다.  
- 현재 목표:  
- 진행 중:  
- 다음 작업(Top 3):  
- 보류/리스크:  
- 최근 변경 요약:  
- 테스트/실행:  
- 중요한 경로:  
- 마지막 업데이트: YYYY-MM-DD HH:MM  

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
