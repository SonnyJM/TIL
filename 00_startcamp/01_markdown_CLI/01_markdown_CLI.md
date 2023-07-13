# CLI
- Command Line Interface


- 새 폴더 만들기 (make directory = mkdir)
```bash
$ mkdir new_folder
```

- 작업 위치를 new_folder로 이동 (cd = change directory)
```bash
$ cd new_folder/
```

- 현재 작업 위치를 열기
```bash
# . -> 현재 위치 (상대 경로)
# 현재 위치를 GUI로 열기
$ start .


# 현재 위치를 VSCODE 로 열기
## 자주 사용할 확률 높음
$ code .
  # 단점 : 이름 잘못 썼을 때에, 오타 발생시 신규 파일 생성
```

-현재 작업 위치의 파일 목록
```bash
$ ls
```

- 파일의 이름을 바꾸거나 위치를 옮기거나
```bash
$ mv {이동할 대상} {이동될 위치}
$ mv {이름 바꿀 대상} {바꿀 이름}
```

## 상대 경로와 절대 경로
### 1. 절대 경로
- 처음부터 끝까지 모든 경로를 다 적어둔 것

    ex) /c/Users/SSAFY/DESKTOP/new_folder

### 2. 상대 경로
- 나를 기준으로 경로를 지정

    ex) . (현재 위치), .. (상위 폴더)


- 삭제(remove)
```bash
$ rm {파일명}
$ rm -r {폴더}
## 완전 삭제 (복구 불가)
### r = 리커전(재귀 : 본디의 것으로 돌아오는 것) (자기 자신을 호출)
```

명령어에서 -: 약어


