# 진법 변경 (10진수 -> n진수)
print(bin(12)) # 2진수
print(oct(12)) # 8진수
print(hex(12)) # 16진수


print(2 / 3)
print(5 / 3)

a = 3.2 - 3.1 # 0.10000000000000009
b = 1.2 - 1.1 # 0.09999999999999987

# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10) # True

# 2. math 모듈 활용
import math
print(math.isclose(a,b)) # True #둘이 얼마나 가깝냐, 이정도의 차이면 같은 수로 보자고 판단.
# 실수 연산할 때 조심하자!

# 지수(제곱하는 횟수) 표현 / e or E : 10^n
print(314e-2)
print(314e2)

# 철수야 '안녕'
print('철수야 \'안녕\'')


print('이 다음은 엔터\n입니다.')


# f-string
bugs = 'roaches'
counts = 100
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')

print('Debugging {} {} {}'.format(bugs, counts, area)) # 옛날 방식 
print('Debugging %s %d %s' % (bugs, counts, area)) # 더 옛날 방식


# f-string 응용
greeting = 'hi'
print(f'{greeting:^10}')
print(f'{greeting:>10}')
print(f'{3.141592:.4f}')
# search 'f-string advanced'\

my_str = 'hello'

# 인덱싱
print(my_str[1])   # e
# 슬라이싱
print(my_str[2:4]) # ll
# 길이
print(len(my_str)) # 5

print(my_str[:3:-1])

my_list = [1, 'a', 3, 'b', 5]

my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

#합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

# 교집합
print(my_set_1 & my_set_2) # {3}




# 불변과 가변
my_str = 'hello'
#my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)

list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1)
print(list_2)