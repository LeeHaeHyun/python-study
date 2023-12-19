# 내장함수

# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 어떤 함수를 가지고 있는지 표시
# print(dir())
# import random  # 외장함수
# print(dir()) # random을 사용할 수 있게 되었음
# import pickle
# print(dir()) # pickle도 사용할 수 있게 되었음

# import random  # 외장함수
# print(dir(random))  # 랜덤 모듈 내에서 쓸 수 있는 것들

# lst = [1, 2, 3]
# print(dir(lst)) # 리스트 모듈 내에서 쓸 수 있는 것들

# name = "Jim"
# print(dir(name))  # name 모듈 내에서 쓸 수 있는 것들

# 구글에서 list of python builtins
# 파이썬 내에 쓸 수 있는 내장함수를 볼 수 있다.

# 외장함수
# 구글에서 List of Python modules

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob

# print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os

# print(os.getcwd())  # 현재 디렉토리
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())  # 모든 파일 조회

# time : 시간 관련 함수 제공
# import time

# print(time.localtime())
# print(time.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

# import datetime

# # print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()  # 오늘 날짜 저장
# we = datetime.datetime(2023, 3, 3)
# td = datetime.timedelta(days=100)  # 100일 저장
# sum = we + td
# print(
#     "우리가 만난지 100일 : "
#     + str(sum.year)
#     + "년 "
#     + str(sum.month)
#     + "월 "
#     + str(sum.day)
#     + "일 "
# )

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈
# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
import byme

byme.sign()

# (출력 예제)
# 이 프로그램은 이해현에 의해 만들어졌습니다.
# 전화번호 : 010-9995-3475
# 이메일 : haehyun93@naver.com
