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


## 3. **Repository**
    - 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역
    - 모든 버전과 변경 이력이 기록됨
    - **commit**
        - 변경된 파일들을 저장하는 행위
    - Repository의 분류
        - local : 현재 작업 영역
        - remote : "원격 저장소" / github & gitlab
            - github/gitlab은 서비스일 뿐 not git!






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
-> commit의 작성자 정보.
-> commit 내용에 관련 정보가 남음.
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

    230712 markdown & CLI 기초 문법과 ChatGPT Bot Programming

한 줄로 보기
$ git log --oneline
```

### 직전 git commit명 수정하기
```
$ git commit --amend

# vim에서 내용 수정하기
# 1. insert를 눌러서 - 삽입 상태로 만든다.
# 2. 커밋 메시지를 수정한다.
# 3. esc를 눌러서 - 삽입 상태를 종료한다.
# 4. :wq를 입력해서 저장하고 종료한다.
```

### git 설정 초기화
```
# vim을 활용해서 설정 제거하기
# vim git 설정 파일 열기
$ vim ~/.git config 
# insert 키 : 수정 상태 만들기
# --insert-- 인 상태에서 모든 내용 삭제
# esc: 수정 상태 종료
# :wq
# insert 상태 아닐 때 u 입력시 작업 취소

$ code ~/.gitconfig
```

### 연습하기!
```
1. 바탕화면에서 vscode 열기
2. vscode에서 bash 터미널 열기
3. bash에서 CLI로 폴더 'git_study' 만들기
4. git_study 폴더 안에 CLI로 파일 'README.md' 만들기
5. vscode에서 README.md 내용 수정하기
6. git init add commit
    6-1. git 기본 설정 (email, name 설정)
7. commit 최소 3개 이상 만들기
```

## Remote Repository
원격저장소 : git을 원격으로 저장할 수 있는 공간

저장하기
```
git remote add origin {주소}
git push -u origin master

(저장 확인)
git remote -v
```
### 주의할 것
1. remote repository
    - .git의 변동사항을 올리는 것!
    - 버전(commit)을 쌓고 -> push 명령어로 올려준다.
    - Add a README file 옵션 지정시, 원격 저장소에 .git이 있는 상태로 생성.
    - 다른 뿌리이기 때문에 local에 생성한 .git이 있는 경우 연동 불가
    - Add a README file 옵션 지정 == git init 명령어를 원격 저장소에 쓴 것.
    - 잘못 만들면 settings -> 삭제

    - github 메일 연동기능 있음.
    - PC 변경시 config 메일/이름 꼭 확인!

### 원격 저장소에 등록
```bash
$ git remote add {remote_nickname} {remote_url} 
```

### 원격 저장소에 업로드
```bash
$ git push origin master
```

### 원격 저장소에 있는 내용 복제
- 최초로 내려받을 때
```bash
$ git clone repository_url
```
- commit 업데이트 할 때
```bash
$ git pull origin master
```