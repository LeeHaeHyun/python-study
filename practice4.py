# # 키, 벨류 사전
# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])  # 유재석
# print(cabinet[100])  # 김태호

# print(cabinet.get(3))  # 유재석
# # print(cabinet[5])  # 에러 발생시키고 끝낸다
# print(cabinet.get(5))  # None을 출력하고 잇는다.
# print(cabinet.get(5, "사용 가능"))  # None 대신 사용 가능을 출력한다.

# print(3 in cabinet)  # True : 캐비넷에 3번 키가 있느냐
# print(5 in cabinet)  # Fale : 캐비넷에 5번 키가 있느냐

# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"  # 초기화하여 유재석이 빠지고 김종국
# cabinet["C-20"] = "조세호"  # 업데이트하여 추가
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]  # 키값 삭제
# print(cabinet)

# # KEY 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key와 value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()  # 모두 지워버림
# print(cabinet)

# 튜플 : 리스트와 다르게 내용 변경이나 추가를 할 수 없음, 속도가 리스트보다 빠름
# 소괄호()를 사용하여 만든다
# menu = ("돈까스", "치즈까스")
# print(menu[0])  # 돈까스
# print(menu[1])  # 치즈까스

# # menu.add("생선까스") # 수정 및 추가가 불가능함: 에러발생

# # 다중 튜플 만들기
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name)
# print(name, age, hobby)

# 집합(set) : 집합, 중복이 안되고 순서가 없음, 중괄호로 만듬
# my_set = {1, 2, 3, 3, 3}
# print(my_set)  # 1,2,3

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 ( 자바와 파이썬을 모두 할 수 있는 사람을 출력해라)
# print(java & python)  # 유재석
# print(java.intersection(python))  # 유재석
# print(python.intersection(java))  # 유재석

# # 합집합 ( java 할 수 있거나 python을 할 수 잇는 개발자)
# print(java | python)  # 김태호 박명수 유재석 양세형
# print(java.union(python))  # 김태호 박명수 유재석 양세형

# # 차집합 ( java 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)  # 양세형 김태호
# print(java.difference(python))

# # python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊어버렸어요
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍 set
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))  # 셋{} 타입으로 바뀜

# menu = list(menu)
# print(menu, type(menu))  # 리스트[] 타입으로 바뀜

# menu = tuple(menu)
# print(menu, type(menu))  # 튜플() 타입으로 바뀜

# menu = set(menu)
# print(menu, type(menu))  # 셋{} 타입으로 바뀜

# Quit) 파이썬 코딩대회 주최
# 댓글 이벤트를 진행하기로 함, 1등 치킨, 3명은 커피 쿠폰 추첨 프로그램을 작성

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위 추첨하되 중복 불가
# 조건3 : random 모듈과 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다. --

# (활용예제)
from random import *

# lst = [1, 2, 3, 4, 5]  # 리스트를 만들고
# print(lst)
# shuffle(lst)  # 섞는 함수 랜덤으로
# print(lst)
# print(sample(lst, 1))  # lst 리스트에서 1개를 무작위로 뽑는 함수

users = range(1, 21)  # 범위 1부터 20까지
# print(type(users))
users = list(users)  # 타입이 range로 나와서 리스트로 바꿔준다.
# print(type(users))
print(users)
shuffle(users)  # 1부터 21까지의 숫자를 랜덤으로 섞어준다.
print(users)

winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")
