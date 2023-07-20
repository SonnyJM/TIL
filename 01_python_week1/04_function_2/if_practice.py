num = int(input('숫자를 입력하세요 : '))

# if statement(if 조건)
# num이 홀수라면 (2로 나눈 나머지가 1이라면)
# if num % 2: 조건문도 가능함. 결과가 1이기 때문에 True! but 후자가 더 명시적.
if num % 2 == 1:
    print('홀수입니다.')
# num이 홀수가 아니라면(짝수면)
else:
    print('짝수입니다.')
