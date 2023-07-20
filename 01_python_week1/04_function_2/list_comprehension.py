

# 0~9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)
print(new_list)

# 2. list comprehension
new_list_2 = [i for i in range(10)] # [(뭐가 들어갈 지) for (인자) in iterable]
print(new_list_2)

new_list_2 = [i for i in range(10) if i % 2 == 1] # [(뭐가 들어갈 지) for (인자) in iterable]
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)] #else가 추가될 경우, 조건문이 앞으로.
print(new_list_2)
print(new_list_3)

#elif는 쓸 수 없음
#if는 뒤로 더 붙일 수 있음!


# 리스트를 생성하는 3가지 방법 비교
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 뭐가 제일 빨라요?
# -성능 => 일반화가 불가능함 (외부 요인, 상황)
# -loop & map & comprehension
# -대부분의 상황에서는 compre가 빠르다
# -하지만 다른 함수, 내장 함수에 따라 map이 더 빠른 경우도 많았음
# -파이썬이 3점대 후반에 for loop 성능에 비약적인 향상이 있었음
# -그래서 극단적인 차이는 존재하지 않음.
# -항상 가독성에 주의합시다...
# - 프로그래밍은 우리 프로그램이 어떻게 그 목적을 명확히 전달하냐에 대한 것

numbers = ['1', '2', '3']

# 1. for loop (일반적인 반복문)
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers) # [1, 2, 3]

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2) # [1, 2, 3]

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3) # [1, 2, 3]




# enumerate
result = ['a', 'b', 'c']

print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]
# 튜플의 언팩킹 과정
for index, elem in enumerate(result):
    print(index, elem)