def greeting(name, age):
    print(f'안녕, {name}, {age}!!')


greeting('Alice', 25)

greeting(25, 'Alice') #안녕, 25, Alice!!

greeting(age = 25 , name = 'Alice') # 인자를 맞춰주면, 순서 상관없이 작동

#greeting(age = 25, 'Dave')
# positional argument follows keyword argument
# "문법 에러"

print('hi', 'aaa', 'bbb', 'ccc')
# 인자의 갯수를 임의의 개수를 받을 수 있도록 정의되어 있음.

def calculate_sum(**kwargs):
    print(kwargs)

calculate_sum(name = 'Alice', age = 30, address = 'Korea')


print(sum([1, 2, 3])) # 6



sum = 10

print(sum)     #10

print(sum([1, 2, 3]))

a = 1
b = 2



def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)    # 10, 2, 500

    local(500)
    print(a, b, c)    # 10, 2, 3

enclosed()
print(a, b)    # 1 2

