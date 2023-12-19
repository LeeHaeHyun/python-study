# 리스트 [] : 순서를 가지는 객체의 집합 ( 대괄호를 씀 )

# 지하철 칸 별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번쨰 칸에 타고 있는가?
# print(subway.index("조세호"))  # 1번째

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")  # 하하가 추가됨
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 탐
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())  # 하하를 뺌
# print(subway)

# print(subway.pop())  # 박명수를 뺌
# print(subway)

# # 같은 이름의 사람이 몇명 있는지 확인
# subway.append("유재석")  # 유재석 추가
# print(subway)
# print(subway.count("유재석"))  # 2가 나온다.

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)  # 1,2,3,4,5

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)  # 5,4,3,2,1

# # 모두 지우기
# num_list.clear()
# print(num_list)  # 비었다.

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)  # 앞뒤로 합침
print(num_list)
