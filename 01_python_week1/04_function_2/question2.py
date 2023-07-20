numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for number in numbers: # number | [1, 2, 3] | [4, 5, 6] | [7, 8, 9]
    for num in number:
        print(num)
    print('=' * 30)

# 문제는, 순서대로만 출력 가능하다는 점.

# 다른 접근

numbers = [
#    0  1  2
    [1, 2, 3], # 0

#    0  1  2
    [4, 5, 6], # 1

#    0  1  2
    [7, 8, 9]  # 2
]

for numbers_index in range(len(numbers)):
    #print(numbers_index)
    scores = numbers[numbers_index]
    for scores_index in range(len(scores)):
        print(numbers[numbers_index][scores_index])

for numbers_index in range(len(numbers)):
    #print(numbers_index)
    scores = numbers[numbers_index]
    for scores_index in range(len(scores)):
        print(numbers[scores_index][numbers_index])