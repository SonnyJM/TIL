def my_func(x):
    result = x * 2
    return result






numbers = [1, 2, 3]
result = map(my_func, numbers)

print(list(result))


result = []
for number in numbers:
    result.append(str(number))

print(result)

names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
cities = ['New York', 'London']

for name, age, city in zip(names, ages, cities):
    print(f'{name} is {age} years old and lives in {city}.')



# map + lambda
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)


def func_name(parm1, parm2):

    return parm1, parm2

func_name(1, 2) # 함수를 호출한 것
# 함수를 호출하는 행위 -> 평가 후 값을 내는 표현식
print(func_name(1, 2))


def greeting(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요!')

# 모든 매개 변수에 키워드 인자 형식으로 값을 할당했을 때만!
greeting(age=30, name='홍길동')

print('첫', '두', '새', end ='\t', sep=':')


# 가변인자로 매개변수를 정의하면
# 함수를 호출할 때, N개의 값을 넘겨도 모두 하나의 변수에 할당
# 이때, tuple 형태로 할당 된다.
def func(*args, sep = ' '):
    print(args, sep)

func('첫', '두', '새')