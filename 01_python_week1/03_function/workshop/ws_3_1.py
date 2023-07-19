number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

# 다른 접근법
# def increase_user(number_of_people):
#     number_of_people += 1
#     return number_of_people

increase_user()
# 다른 방법을 썼을 경우
# number_of_people = increase_user()
print('현재 가입 된 유저 수 :', number_of_people)


# local에서는 조회할 때만 global로 찾아감. 작동시에는 상위 스코프 값을 먼저 건드리지 않음.
# 방법 1 : global 키워드 사용하기
# 방법 2 : 인자로 집어넣고 리턴해서 함수를 호출한 결과를 재할당하기.
