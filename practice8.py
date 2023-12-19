# 파일 입출력

# 파일 쓰기
# score_file = open(
#     "score.txt", "w", encoding="utf8"
# )  # 인코딩을 하는 이유: 한글깨짐 방지, "w" = write 쓰는 용도
# print("수학 : 0", file=score_file)  # 파일 안에 씀
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")  # .write는 줄바꿈이 없기에 줄바꿈 처리
# score_file.close()

# # 파일 읽기
# score_file = open("score.txt", "r", encoding="utf8")  # "r" = read 읽는 용도
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")  # "r" = read 읽는 용도
# print(score_file.readline())  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline(), end="")  # 줄바꿈을 안하고 싶다면 end 처리
# print(score_file.readline())
# score_file.close()

# 몇 줄인지 모를 파일을 읽을 때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:  # 무한반복
#     line = score_file.readline()  # 한줄씩 읽는데 변수에 넣음
#     if not line:  # 라인이 없을 경우
#         break  # 빠져나옴
#     print(line, end="")  # line 변수 출력
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # list 형태로 저장
# print(type(lines))  # list라고 타입 확인
# for line in lines:  # 리스트를 line에 넣어서 for문을 통해 출력
#     print(line, end="")

# score_file.close()

# pickle
# import pickle

# 피클 쓰기
# profile_file = open("profile.pickle", "wb") # wb : 바이너리를 씀
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# 피클 읽기
# profile_file = open("profile.pickle", "rb")  # rb : 바이너리를 읽음
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with
# import pickle

# with open(
#     "profile.pickle", "rb"
# ) as profile_file:  # profile.pickle을 profile_file의 변수에 저장
#     print(pickle.load(profile_file))  # 피클로드를 통해 출력

# with문을 뜨면 닫을 필요없음 자동으로 종료해줌

# with로 파일 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with로 파일 읽기
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())  # close할 필요가 없음

# Quiz) 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약 :

# 1주차부터 50주차 까지의 보고서를 만드는 프로그램을 작성하시고
# 조건: 파일명은 '1주차.txt','2주차.txt', ... 와 같이 만든다.

for i in range(1, 51):  # 반복문이 필요
    with open(
        str(i) + "주차.txt", "w", encoding="utf8"  # w모드가 있기에 쓰기모드로써 기존에 파일이 있어도 덮어쓰기한다.
    ) as report_file:  # close를 안하기 위해서 with로
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서:")
        report_file.write("\n이름:")
        report_file.write("\n업무 요약 :")
