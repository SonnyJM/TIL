#while True:
#    print('점심시간')
#    print('점심시간 끝')

# 위 식대로 넣으면 무한 반복,종료 조건을 꼭 만들어줘야 함.

# 5번만 반복되도록 하고 싶다
# type 1
#result = 0
#while result != 5:
    #print('점심시간')
    #print('점심시간 끝')
    #print(result)
#    result += 1
#    for i in range(3):
#        print(i)

#    print(result)

dust = [1, 2]
result = 0
while result != 5:
    #print('점심시간')
    #print('점심시간 끝')
    #print(result)
    result += 1
    for i in range(2):
        print(dust[i], 'for')

    print(result, 'while')

# 문제 풀고 답변 제출하기 전, print 문 안에 내가 이해할 수 있는 텍스트 기록 남기기.