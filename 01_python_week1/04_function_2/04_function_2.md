# Function part 2 (함수와 제어문 2)
20230720

## Control of Flow (제어문)

### 제어문 (control statement)

코드의 실행 흐름을 제어하는 데 사용되는 구문

**조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행

### 조건문 (Conditional Statement)

주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

if / elif / else

파이썬 조건문에 사용되는 키워드

if statement의 기본 구조

```bash
if 표현식:
    코드 블록
elif 표현식:
    코드 블록
else:
    코드 블록
# else는 표현식이 없음. 위의 조건들을 다룬 후 나머지를 뜻함.
```

- 조건문 예시
```bash
a = 5

if a > 3:       
# 비교 평가 후 True로 평가되면, else는 의미 없어짐.
# False일 경우, 다음 조건문으로 넘어감.
    print('3 초과')
else:
    print('3 이하')

print(a)
```

- 복수 조건문 예시
  - 조건식을 동시에 검사하는 것이 아니라, 순차적으로 비교
```bash
dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
# 위에서부터 순차적으로 차례차례 비교검사하여 내려온다
```

- 중첩 조건문 예시
```bash
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```
---
### 반복문 Loop Statement
주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행

    -> 특별한 종료 조건이 없음
- 주어진 조건이 참인 동안 반복

     => 조건이 False가 되면 멈춤

### for
임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

-> 더 정확히는, '반복 가능한 객체(iterable)'는 다 가능함.

-> Sequence는 길이가 있고, 갯수가 정해져 있기 때문에 종료조건이 필요하지 않음

- for statement의 기본 구조
```bash
for 변수(임시변수) in 반복 가능한 객체:
    코드 블록
# [1, 2, 3]을 넣는다고 했을 때,
# '1'이 변수 할당 -> 코드 블록 실행 -> '2' 할당 -> 실행 -> '3' 할당 -> 실행
# 반복 가능한 객체의 요소 수만큼 반복.
```

**반복 가능한 객체 iterable**
반복문에서 순회할 수 있는 객체

(시퀀스 객체 뿐만 아니라 dict, set 등도 포함)

### for 문 원리
- 리스트 내 첫 항목이 반복 변수에 할당되고

```bash
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)
  
#apple, banana, coconut
```
- 문자열 순회
```
country = 'Korea'

for char in country:
    print(char)
  
'''
K
o
r
e
a
'''
```

- range 순회
```bash
for i in range(5):
    print(i)
# 5까지가 아니라 4까지!

'''
0
1
2
3
4
'''

```

- 인덱스로 리스트 순회
    - 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
```bash
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)): # len 함수를 쓴 이유 : 재사용 할 수 없기 때문. 수치를 고정하면 다른 input값이 정해졌을 때 대응하기 어려움.
    numbers[i] = numbers[i] * 2

print (numbers)
```

- 중첩된 반복문(2)
  - 중첩된 반복문 출력 예상해보기
  - 안쪽 반복문은 outer 리스트의 각 항목에 대해 한 번씩 실행됨
  - print가 호출되는 횟수 => len(outers) * len(inners)
```bash
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:     #inner 반복문이 끝나고 진행
    for inner in inners: #안쪽 반복문이 끝나야 ↑
        print(outer, inner)
'''
A, C
A, D
B, C
B, D
'''
```

- 중첩 리스트 순회
  - 안쪽 리스트 요소에 접근하려면, 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
```bash
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)
'''
['A', 'B']
['C', 'D']
'''


#안쪽까지 중첩을 뽑는 방법
for elem in elements:
    for item in elem:
        print(item)
```

## 'while' statement
주어진 조건식이 참(True)인 동안 코드를 반복해서 실행

== 조건식이 거짓(False)가 될 때까지 반복 (접근법!)

- while statement의 기본 구조
```bash
while 조건식:
    코드 블록
```

- while 반복문 예시
```bash
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

'''
0
1
2
끝
'''
```
- 조건 설정 잘 할 것!

- 특정 입력 값에 대한 종료 조건 활용하기
```bash
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')
```

#### while문은 반드시 종료 조건이 필요!!

### 적절한 반복문 활용하기
- for
    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

- while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복

---

## 반복 제어
for 문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만, 때때로 일부만 실행하는 것이 필요할 때가 있음

- **break**
  - 반복을 즉시 중지
-  **continue**
  - 다음 반복으로 건너뜀

- break 예시
```bash
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break    ### 더이상 반복하지 않고, 아예 종료해버림.

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')
```

- 리스트에서 홀수만 출력하기
  - 특정한 값을 찾으면, 더이상 조사하지 않을 때
```bash
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다: ', num)
        found_even = True
        break # "6을 찾았기 때문에, 끝남"

if not found_even:
    print('짝수를 찾지 못했습니다')
```

- continue 예시
```bash
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue # 다음 코드 블록이 아니라, 다음 반복으로 건너뛰기!! 주의. 여기서는 아래의 print(num)이 작동하지 않음
    print(num)
```

### break, continue 주의사항
- break와 continue 남용은 코드의 가독성 저하
- **특정한 종료 조건**을 만들어 break를 대신하거나, **if 문을 사용**해 continue 처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지, 코드의 의도를 명확하게 작성하도록 노력해야 함.


### List Comprehension
간결하고 효율적인 **리스트 생성** 방법

#### List Comprehension 구조
```bash
[expression for 변수 in iterable]
==
list(expression for 변수 in iterable)

## 방식은 이해하되 이 이상으로 복잡하게 쓰진 맙시다,,,
```

- 효율적이고 간결하진 하지만... 가독성과 직관성은 떨어지는 편

- 두 종류의 방식을 서로 바꾸는 방법을 알고 있어야 함

#### Comprehension을 남용하지 말자

*Simple is better than complex*

*Keep it simple, stupid*

### pass
아무런 동작도 수행하지 않고 넘어가는 역할
- 문법적으로 문장이 필요하지만, 프로그램 실행에는 영향을 주지 않아야 할 때 사용.

- pass 예시

1. 코드 작성 중 미완성 부분

2. 조건문에서 아무런 동작을 수행하지 않아야 할 때

3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법.


### enumerate

```bash
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enemurate(fruits)
```



*"작은 효율성에 대해서는, 말하자면 97% 정도에 대해서는, 잊어버려라. 섣부른 최적화는 모든 악의 근원이다." - Donal Knuth*