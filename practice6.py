# 함수 정의
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):  # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money


# def withdraw(balance, money):  # 출금
#     if balance >= money:  # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금에 실패하였습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# commission = 100  # 수수료 100원


# def withdraw_night(balance, money):  # 저녁에 출금
#     if balance >= money + commission:  # 잔액이 수수료를 포함하여 출금보다 많으면
#         return commission, balance - money - commission
#     else:
#         print("수수료 {0}원이 부족합니다. 잔액은 {1} 원입니다.".format(commission, balance))
#         return balance


# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# print(balance)
# # balance = withdraw(balance, 2000) # 출금 실패
# balance = withdraw(balance, 500)

# balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 함수의 기본값
# def profile(name, age=17, main_lang="파이썬"):  # 기본값, 주사용언어를 설정
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))


# # profile("유재석", 20, "파이썬")
# # profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업
# profile("유재석")
# profile("김태호", 25)


# 키워드값 ( 순서가 바뀌어도 상관없다 )
# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


# 가변인자를 통한 함수호출
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")  # end는 줄바꿈없이 빈칸으로 끝난다
#     print(lang1, lang2, lang3, lang4, lang5)


# def profile(name, age, *language):  # *language가 가변인자 : 특징 for문으로 출력한다.
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")  # end는 줄바꿈없이 빈칸으로 끝난다
#     for lang in language:
#         print(lang, end=" ")
#     print()  # 줄바꿈을 위한 프린트

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "Kotlin", "Swift")

# 전역 변수와 지역변수
# gun = 10 # 전역변수 정의


# def checkpoint(soldiers):  # 경계 근무
#     gun = 20  # 지역 변수인 gun을 사용: 결과는 18이 됨
#     # global gun  # 전역 변수인 gun을 사용: 결과는 8이 됨// 되도록이면 전역변수보다 지역 변수를 사용함
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))


# print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun # 계산된 남은 총을 return을 통해 반환


# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2) # 전역변수인 gun을 함수로 전달
# print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성
# # 표준체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.


# def std_weight(height, gender):  # 키는 m단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)  # 소수 둘째자리에서 반올림
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
