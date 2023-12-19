# 연산 출력하기
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5 + 3)
# print(5 * 8)
# print(3 * (3 + 1))

# 문자열 출력하기
# print("풍선")
# print("나비")
# print("ㅋ" * 10)  # 문자 x10을 하면 그 문자가 10번 출력된다.

# 참/거짓 bealean
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))  # true

# 변수
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "낮잠"
# is_adult = age > 3  # 나이가 3이상이면 어른이다.

# print("우리집 " + animal + "의 이름은 " + name + "이에요")
# hobby = "공놀이"
# print(
#     name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요"
# )  # +로 감싼다면 정수형은 str로 감싸줘야 오류가 안나고 출력된다.
# print(
#     name, "는", age, "살이며", hobby, "을 아주 좋아해요"
# )  # ,로 진행한다면 str을 안써도 출력되며 띄어쓰기가 필수로 함께 출력된다.

# print(name + "는 어른일까요? " + str(is_adult))

# 주석
# 컨트롤 + / 도 되며
"""안녕 반가워
안녕 안녕"""  # 작은따옴표 3개로 주석처리할 수 있다.

# Quiz) 변수를 이용해서 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : xx 행 열차가 들어오고 있습니다.

# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

# 연산자 종합
# print(1 + 1)  # 2
# print(3 - 2)  # 1
# print(5 * 2)  # 10
# print(6 / 3)  # 2.0

# print(2**3)  # 2^3 = 8

# # 나머지 구하기
# print(5 % 3)  # 2
# print(10 % 3)  # 1

# # 몫 구하기
# print(5 // 3)  # 1
# print(10 // 3)  # 3

# # 부등호
# print(10 > 3)  # True
# print(4 >= 7)  # False

# # 같다
# print(3 == 3)  # True
# print(4 == 2)  # False
# print(3 + 4 == 7)  # True

# # 같지 않다
# print(1 != 3)  # True
# print(not (1 != 3))  # False

# # and 조건 : 둘다 만족해야 True
# print((3 > 0) and (3 < 5))  # True
# print((3 > 0) & (3 < 5))  # True

# # or 조건 : 둘 중 하나만 만족하면 True
# print((3 > 0) or (3 > 5))  # True
# print((3 > 0) | (3 > 5))  # True

# print(5 > 4 > 3)  # True
# print(5 > 4 > 7)  # False

# 수식
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20

number = 2 + 3 * 4
print(number)

number = number + 2  # 16
print(number)

number += 2  # 18
print(number)

number *= 2  # 36
print(number)

number /= 2  # 18
print(number)

number -= 2  # 16
print(number)

number %= 5  # 1
print(number)
