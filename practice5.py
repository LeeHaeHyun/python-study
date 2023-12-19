# if 조건
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("날씨가 좋습니다.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨네요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지마세요")

# for 반복문
# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# randrage()
# for waiting_no in range(2, 10):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 페기처분 되었습니다.")


# 무한루프 빠져나오기 : 터미널에 컨트롤 + c (강제종료)
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# continu와 break
# absent = [2, 5]  # 결석
# no_book = [7]  # 책을 안가져옴
# for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue  # 이 구문을 만나면 아래를 실행하지 않고 위로 돌아간다.
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
#         break  # 이 구문을 만나면 끝내버림
#     print("{0}, 책을 읽어봐".format(student))

# 한줄 for
# 출석 번호가 1,2,3,4 인데 앞에 100을 붙이기로 함 -> 101,102,103,104
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [
#     i + 100 for i in students
# ]  # students에 리스트에 있는 것들을 하나씩 불러넣으면서 i에 넣고 +100을 더해라
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대분자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# Quiz) Cocoa 서비스를 이용하는 택시 기사
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건1: 승객별 운행 소요시간 5~50분 사이의 난수
# 조건2: 소요시간 5분~15분 사이의 승객만 매칭

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [] 2번째 손님 (소요시간: 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [] 50번쨰 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *

cnt = 0  # 총 탑승 승객수
for i in range(1, 51):  # 1 ~ 50이라는 수 (승객)
    time = randrange(5, 51)  # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한경우
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))
