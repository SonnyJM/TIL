# Git 이란?
> 분산 버전 관리 시스템

**분산** : 퍼뜨려서

**버전 관리** : 변화를 기록하고 추적하는 것

```
#### 버전을 관리하는 방법

분산식 관리
    - 버전을 여러 개의 복제된 저장소에 저장 및 관리

<-> 중앙 집중식 관리
    - 버전은 중앙 서버 저장, 중앙 서버에서 파일을 가져와 다시 중앙에 업로드

    **분산 구조 장점**
    - 중앙 서버 의존 없이 다양한 작업 수행
```

### Git의 역할
- 코드의 버전(히스토리) 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

## Git의 영역
1. **Working Directory**
    - 실제로 작업하고 있는 환경
    - Git이 수정할 작업이 일어나고 있는 곳
 
2. **Staging Area**
    - Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역


3. **Repository**
    - 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역
    - 모든 버전과 변경 이력이 기록됨
    - **commit**
        - 변경된 파일들을 저장하는 행위
### git 초기화
```
$ git init
```

### 상태 확인 명령어
```
$ git status
```

### git에 추가 명령어
```
$ git add {path}<folder_name>/{file_name}
```

### Repository에 저장하기
```
$ git commit -m "commit message"
```
- commit message는 상세히 남기면 좋음
- 공백이 의미하는 바 생각하기!
- 따옴표 감싸기 가능. (문자열 만들기)
```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```
### git 기초 설정
```bash
$ git config --global user.email "kain9101@naver.com"
$ git config --global user.name "손종민"

$ git config --global --list
```

터미널 단축키
- 복사 : 우클릭
- 붙여넣기 : shift + insert

### 커밋 기록 확인하기
```
$ git log
```

```
$ git log
commit 84b333f46d4eecaf78c8222109aa44bb0633157b (HEAD -> master) # commit 고유값
Author: 손종민 <kain9101@naver.com>
Date:   Thu Jul 13 11:09:25 2023 +0900

    230712 markdown & CLI 기초 문법과 ChatGPT Bot Programming```

``````
### 직전 git commit명 수정하기
```
$ git commit --amend

# vim에서 내용 수정하기
# 1. insert를 눌러서 - 삽입 상태로 만든다.
# 2. 커밋 메시지를 수정한다.
# 3. esc를 눌러서 - 삽입 상태를 종료한다.
# 4. :wq를 입력해서 저장하고 종료한다.
```
