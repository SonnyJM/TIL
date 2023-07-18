## index 접근이라는 것을 할 수 있다.
# index 접근이란 건... 어디에? list, str 등 순서가 있는 sequence 자료형
# 슬라이싱이란..?
#      0  1  2  3  4
#      ㅣ ㅣ ㅣ ㅣ |
list = [1, 2, 3, 4, 5]
print(list[1 : 4 : 1]) # [2, 3, 4] = 왜 잘랐는데 값이 나오는지?
print(list[1 : 4 : 2]) # [2, 4]
print(list[1 : 4 : 3]) # [2]
# 슬라이싱 쓸 때는 범위 벗어나도 오류 없이 잘 나오니까 주의하자.
# list[start : end : step]
# | start에 작성한 내용은 그 index 번호부터 시작.
# | end에 작성한 내용은 그 index - 1 번째까지만 출력
# | step에 작성된 내용은, start부터 end까지 step만큼 건너뛰면서.
# | range에도 똑같이 활용. range(start, end, step)
print(list[1 : 100])