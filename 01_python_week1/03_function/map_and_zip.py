def some_func(parm1):
    return parm1 ** 2

print(some_func(3))
print(some_func)

other_var = some_func
print(other_var(3))

numbers = [3, 6, 9]
print(list(map(other_var, numbers)))

# map 함수를 쓸 때 변수가 하나면 오브젝트가 그대로 반환되고, 변수가 여러 개면 언패킹이 되는 건가요?

def my_map(func, iterable):
    for item in iterable:
        result = func(item)
        print(result, end=' ')

my_map(some_func, numbers)