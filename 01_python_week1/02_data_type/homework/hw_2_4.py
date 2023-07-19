authors = ['작자 미상', '이항복', '임제', '임제', 
           '조성기', '조성기', '조성기', '임제', 
           '허균', '허균', '허균', '임제', '임제', 
           '임제', '임제', '임제', '임제', '임제', 
           '임제', '임제', '임제', '박지원', '이항복', 
           '남영로', '남영로', '남영로', '이항복', '임제', '임제']

print(list(set(authors))[::-1])
# 답안이 이미 설정되어있어서 commit이 불가능해서, 리스트 다루는 연습 해봤습니다!

# list -> set -> list
# set : 중복 없는 논-시퀀스형 데이터

# 반복문을 통해서 중복이라는 사실을 알 수 있는 방법?
# ex> '작자 미상'이라는 값이 몇 번 나왔는지 세면 됨.
# new_list를 만들고, 해당 리스트 내에 해당 내용이 아직 들어있지 않을 때 추가해준다.
