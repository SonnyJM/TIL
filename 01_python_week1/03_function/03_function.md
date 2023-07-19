# Functions (함수)

## 함수

**특정 작업을 수행**하기 위한 **재사용 가능**한 코드 묶음

### 함수를 사용하는 이유
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드 중복을 방지
- **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상

### 내장 함수 (Built-in function)

파이썬이 기본적으로 제공하는 함수 (별도의 import 없이 바로 사용 가능)

**내장 함수 예시**
- 절대값을 만드는 함수 abs

### 함수 호출 (function call)

함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

### 함수 구조
INPUT X (Parameter, 매개변수) -> Docstring(설명), function body -> OUTPUT f(x) (return value, 반환값)

### 함수의 정의와 호출
- 함수 정의(정의)
  - 함수 정의는 def 키워드로 시작
  - def 키워드 이후 함수 이름 작성
  - 괄호 안에 매개변수를 정의할 수 있음
  - 매개변수(parameter)는 함수에 전달되는 값을 나타냄

- 함수 body
  - 콜론(:) 다음에 들여쓰기 된 코드 블록
  - 함수가 실행 될 때 수행되는 코드를 정의
  - Docstring은 선택적으로 서술 가능한 함수 설명서

- 함수 반환 값
  - 함수는 필요한 경우 결과를 반환할 수 있음
  - return 키워드 이후에 반환할 값을 명시
  - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
  - 반환 != 출력
  - return 아래로는 의미없음 (종료)
  - 반환값이 없는 함수는 자동으로 return이 None




## 매개변수와 인자
**매개변수(parameter)** : 함수를 **정의**할 때, 함수가 받을 값을 나타내는 변수

**인자(argument)** : 함수를 **호출**할 때 실제로 전달되는 값

```bash

def add_numbers(x, y): # x와 y는 매개변수(parameter)
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers (a와 b는 인자)
```


### 위치인자 (Position Arguments)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
  - *위치인자는 함수 호출 시 반드시 값을 전달해야 함!*
- 위치인자 누락시 호출 불가.

### 기본 인자 값 (Default Argument Values)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

### 키워드 인자 (Keyword Arguments)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당.
- 인자의 순서는 중요하지 않고, 인자 이름을 명시하여 전달.
  - *호출시 키워드 인자는 위치 인자 뒤에 위치해야 함!*
- 기본 인자 값이 있는 것을 썼을 때 의미가 커짐.

### Arbitary Argument Lists (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리.

### Arbitary Keyword Argument Lists (임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용, 여러 개의 인자를 dictionary로 묶어 처리.

**함수 인자 권장 작성순서**
- 위치 -> 기본 -> 가변 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
  - *단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정*


## Python의 범위(Scope)
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : **함수**가 만든 scope (함수 내부에서만 참조 가능)
  - ex> def my_func():
            num = 1
    print(num)
  - 위 예시의 경우, num이 출력되지 않음 (함수 내에서만 참조, 작동)
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

**Scope 예시**

```
 def my_func():
            num = 1
    print(num)
```
- 변수의 수명주기

**변수 수명주기(lifecycle)**
- 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨

**1. built-in scope**
  - 파이썬이 실행된 이후부터 영원히 유지

**2. global scope**
  - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

**3. local scope**
  - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

**이름 검색 규칙(Name Resolution)**
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름

  1. Local scope : 지역 범위(현재 작업중인 범위)
  2. Enclosed scope : 지역 범위 한 단계 위 범위
  3. Global scope : 최상단에 위치한 범위
  4. Built-in scope : 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)

**이름 검색 규칙 예시**
  ```bash
  num = 100
  
  def my_func():
      print(num)
  ```
  위의 코드는 에러가 나지 않음 (밖으로는 찾아 올라갈 수 있음)

  -> 예시일 뿐 코드 이렇게 짜지 마세요......


**'global' 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용.
```bash
num = 0 # 전역 변수

def increment():
    global num # num을 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1
```

- 주의사항
  - global 키워드 선언 전에 접근 X
  - 매개변수에 global 사용 불가
  - 가급적 사용하지 않는 것 권장
  - 함수로 값을 바꾸고자 하면, 항상 인자로 넘기고 함수의 반환 값 사용하는 것을 권장.


## 재귀함수
### 재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들고, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 발생
- 재귀함수 예시 : 팩토리얼
n! = n * (n-1)! = n * (n-1) * (n-2)!

```
f(4) = 4 * f(3)
f(3) = 3 * f(2)
f(2) = 2 * f(1)
f(1) = 1
```

```bash
def factorial(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n-1)

```

재귀함수는
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록!



## 유용한 내장 함수

map(function, iterable(반복가능한 객체))

순회가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환.


zip(*iterables)

임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환


### lambda 함수

이름 없이 사용되는 함수

**lambda 함수 구조**
```bash
lambda 매개변수: 표현식
```

- 파이썬의 명시적인 구조와는 조금 멀어진 느낌,,,


## 패킹 Packing

여러 개의 값을 하나의 변수에 묶어서 담는 것

- 변수에 담긴 값들은 튜플 형태로 묶임
(쓰지마세요... 가독성 떨어집니다...)
- 파이썬 내부적으로 패킹해서 쓰고 있음.

**'*'를 활용한 패킹**
- *b는 남는 요소들을 리스트로 패킹하여 할당

- 가독성 떨어지니... 활용은 조금만...


## 언패킹 Unpacking

패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것.

**언패킹 예시**
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
```bash
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values

print(a, b, c, d, e) # 1 2 3 4 5
```

- *를 활용한 언패킹
```bash
names = ['alice, 'jane', 'peter']
print(*names) # alice jane peter
```

- **를 활용한 언패킹
```bash
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x' : 1, 'y' : 2, 'z' : 3}
my_function(**my_dict) # 1 2 3

```

## 모듈
한 파일로 묶인 변수와 함수의 모음

특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)
- 다른 프로그래머가 이미 적어둔 코드들

## 패키지 Package

관련된 모듈들을 하나의 디렉토리에 모아놓은 것

### pip

외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

- 모듈을 정의하는 경우에 가능하면 이름 안 겹치게
- 부득이한 경우에는 별명을 지어줄 수 있음

```bash
from {module_name} import {vari} as {nickname}
```

- 모듈명은 built-in function과 겹치지 않는 파일 명으로 만들 것.

