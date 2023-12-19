# 문자열
# sentence = "나는 소년입니다."
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])  # 0부터 7번째에 있는 1을 출력한다.
# print("연 : " + jumin[0:2])  # 0~2직전까지 0 1 까지만 가져온다.
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지 가져옴
# print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])
# # 맨 뒤에서 7번쨰부터 끝까지, 맨뒤를 -1로 계산한다.

# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())  # 소문자로 모두 출력
# print(python.upper())  # 대문자로 모두 출력
# print(python[0].isupper())  # 0번째가 대문자인지 확인하는 boolean 함수
# print(len(python))  # 문자열의 길이를 출력한다.
# print(python.replace("Python", "Java"))  # 문자열을 찾아서 바꿔줌

# index = python.index("n")  # n이 몇번쨰에 있는지 찾아라
# print(index)  # 0번째부터 5번째에 있다.
# index = python.index("n", index + 1)  # 두번째 n은 몇번쨰에 있는지 찾아라
# print(index)  # 0번쨰부터 5번쨰를 지나쳐서 15번째에 있다.

# index = python.find("n")
# print(index)  # 0번째부터 5번째에 있다.

# index = python.find("Java")  # 자바가 없으니 -1을 출력하고 프로그램은 계속 이어진다.
# print(index)
# # index = python.index("Java")  # 자바가 없으니 에러를 낸다

# print(python.count("n"))  # n이 총 몇번 등장하는지 알려준다 #2가 출력

# 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1 : %d와 %s와 %c 를 이용
# print("나는 %d살입니다." % 20)  # d는 정수를 의미해서 정수만 넣을 수 있다.
# print("나는 %s을 좋아해요" % "파이썬")  # s는 String 문자열만 가능
# print("Apple은 %c로 시작해요." % "A")  # c는 char로 1글자만 넣을 수 있음

# %s는 스트링이기에 숫자도 넣을 수 있음
# print("나는 %s살입니다." % 20)  # d는 정수를 의미해서 정수만 넣을 수 있다.
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))  # 2개면 이처럼 ()로 감싼다.

# 방법 2 : {}와 .format 이용
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아합니다.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아합니다.".format("파란", "빨간"))  # {}중괄호안에 숫자를 넣으면 숫자에 맞게 출력됨

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))

# 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요!")  # print앞에 f를 넣어 변수를 대입 시킬 수 있다.

# 탈출문자
# \n : 줄바꿈
# print("백문이 불여일견\n불견이 불여일타")

# # "저는 \"이해현\"입니다" (탈출문자 \)
# print('저는 "이해현"입니다.')

# # \\ : 문장 내에서 \
# print("C:\\Users\\leehaehyun")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스 (한글자를 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예시: http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
# url = "http://youtube.com"
url = "http://google.com"
my_str = url[7:]  # 규칙1 : 슬라이스
my_str = my_str.replace(".com", "")  # 규칙2 : replace
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
