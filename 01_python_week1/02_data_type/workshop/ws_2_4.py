information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

'''
- 작가와 작품 목록 참고
- 허균 : 홍길동전, 장생전, 도문대작
- 임제 : 수성지, 백호집, 원생몽유록
- 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
'''

information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

list_info = list(information)

print(list_info[0],':', information['김시습'])
print(list_info[1], ':', information['허균'])
print(list_info[2], ':', information['남영로'])
print(list_info[3], ':', information['작자 미상'])
print(list_info[4], ':', information['임제'])

# 다른 방법(f string 활용)
print(f'{authors[0]} : {information[authors[0]]}')
'''
ages = [30, 20, 10]
addresss = ['서울', '부산', '광주']

infos = [ages, addresss]
'''