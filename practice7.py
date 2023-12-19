# 표준 입출력
# print("Python", "Java")  # 떨어진다
# print("Python" + "Java")  # 붙는다

# print("Python", "Java", sep=",")  # sep는 사이에 무엇을 넣을지 지정해줄 수 있다.
# print("Python", "Java", "C#", sep=" vs ")  # sep는 사이에 무엇을 넣을지 지정해줄 수 있다.

# print(
#     "Python", "Java", sep=",", end="?"
# )  # sep로 인해 사이에 ,(콤마)가 들어가고 end를 명시해줌으로써 2줄을 한줄로 출력
# print("무엇이 더 재미있을까요?")

# import sys

# print("Python", "Java", file=sys.stdout) # 표준 출력으로 문장이 찍힘
# print("Python", "Java", file=sys.stderr) # 표준 에러로 문장이 찍힘

# 시험 성적
# score = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in score.items():  # 튜플로 보내줌
#     # print(subject, score)
#     print(
#         subject.ljust(8), str(score).rjust(4), sep=":"
#     )  # 8칸의 공간을 확보하고 왼쪽 정렬, 4칸의 공간을 확보하고 오른쪽 정렬


# 은행 대기순번표
# 001,002,003 ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))  #zfill : 3크기만큼 공간을 마련하고 값이 없는 건 0으로 채워라

# answer = input("아무 값이나 입력하세요 : ")  # 인풋으로 받는 값은 항상 문자열 형태로 저장된다.
# print(type(answer))
# # print("입력하신 값은 " + answer + "입니다.") # 문자열 형태이기에 숫자를 입력하더라도 str()로 감싸지 않고 그냥 프린트해도 된다.

# 다양한 출력 포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))  # 10칸을 공간을 마련하고 오른쪽 정렬을 하고 500을 입력한다.
# 양수 일 때 + 표시, 음수일땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))  # 10칸을 확보하고 왼쪽 정렬을 하는데 빈공간은 _ 로 채움
print("{0:_<10}".format(500))  # 양수일때 +가 없이 그냥 500만 찍힘

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 콤마를 찍어주면서 +,- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리마다 콤마를 찍어주고, 부호로 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print(
    "{0:^<+30,}".format(1000000000000000)
)  # 30자리 공간 확보, 3자리마다 콤마, 부호도 붙힘, 왼쪽 정렬, 빈공간은 ^

# 소수점 출력
print("{0:f}".format(5 / 3))  # float,
# 소주점을 특정 자리수 까지만 표시 ( 소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5 / 3))  # 소수점 2자리까지만 표시
