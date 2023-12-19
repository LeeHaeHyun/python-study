# 숫자 처리 함수

# print(abs(-5))  # 5 절대값
# print(pow(4, 2))  # 4^2 거듭제곱= 4x4 = 16
# print(max(5, 12))  # 12 최대값
# print(min(5, 12))  # 5 최소값

# print(round(3.14))  # 3 반올림
# print(round(4.99))  # 5 반올림
# print(round(1.755, 2)) # 소수2째자리에서 반올림

# from math import *  # 파이선의 math 라이브러리의 모든 것을 이용하겠다.

# print(floor(4.99))  # 내림. 4
# print(ceil(3.14))  # 올림. 4
# print(sqrt(16))  # 제곱근 4.0

# 랜덤 함수
from random import *

# print(random())  # 0.0 이상 1.0 미만의 임의의 값을 생성
# print(random() * 10)  # 0.0 ~ 10미만의 임의의 값을 생성
# print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46))  # 1~45 이하의 임의의 값이 생성/ 뒷자리 -1를 포함하는 랜덤함수
# print(randint(1, 45))  # 1~45 이하의 임의의 값을 생성/ 앞 자리와 뒷자리를 포함하는 랜덤 함수

# Quiz) 코딩 스터디 모임을 개설, 월 4회 스터디를 하는데
# 3번은 온라인, 1번은 오프라인
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램
# 1: 랜덤으로 날짜를 뽑는다.
# 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 출력문 예제
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# 풀이: 4일~28일 이내로 랜덤 숫자 출력

date = randint(4, 28)
# date는 숫자이기 때문에 문자열 출력인 print 내에서 쓰려면 str로 감싸줘야 한다.
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")
