book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
# 문자열 * 정수가 가능하다
print(int(book) * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(total - int(rental)) # 암묵적 형변환 -> '명시적 형변환'
