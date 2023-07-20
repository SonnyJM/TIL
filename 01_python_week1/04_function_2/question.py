# list -> sequence type data : 순서가 있다
# list -> 길이를 알 수 있따. len(list)
# range -> 0 ~ n-1 까지의 숫자 범위를 만들 수 있다.
# range -> sequence type, iterable
# for 특성 | iterable한 값이 가지고 있는 각 요소들을, 임시 변수에 할당해서 코드 실행
# for 문으로 range를 순회하면, range가 가지고 있는 0부터 n-1 까지의 값을 순회

print(list(range(3)))

for index in range(3):
    print(index)


dusts = [60, 50, 66, 70]
print(len(dusts)) #4
print(range(len(dusts))) # range(0, 4) -> 0, 1, 2, 3
for index in range(len(dusts)):
    print(index)
# 리스트 내에 있는 값들을 수정하기 용이함.
# 대상 자체를 제어하기도 용이함.

for dust in dusts:
    print(dust)
# 리스트 내 값들을 수정하기 어려움.