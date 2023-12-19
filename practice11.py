# # 스타크래프트 프로젝트
# from random import *


# # 일반 유닛 클래스
# class Unit:  # 클래스, 클래스명
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")  # move의 원래 정의
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 공격 유닛 클래스
# class Attackunit(Unit):  # () 안에 클래스명을 넣으면 상속
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)  # 자바의 super과 같음, 물려받을 내용
#         self.damage = damage

#     def attack(self, location):  # self는 자기 자신을 의미, 메소드 앞엔 반드시 self를 적어준다
#         print(
#             "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 마린
# class Marine(Attackunit):
#     def __init__(self):
#         Attackunit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정 시간 동안 공격 속도 증가, 체력 10감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# # 탱크
# class Tank(Attackunit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
#     seize_developed = False  # 시즈모드 개발여부

#     def __init__(self):
#         Attackunit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True

#         # 현재 시즈모드일 때 -> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False


# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(
#             "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
#         )


# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(Attackunit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):  # 실행하기 위한 조건
#         Attackunit.__init__(self, name, hp, 0, damage)  # 지상 스피드는 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):  # unit의 move를 재정의: 메소드 오버라이딩
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False  # 클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True:  # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:  # 클로킹 모드 해제 -> 모드 실행
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     print("Player : gg")  # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 실제 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 ( 마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전국 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음 (5~20)

# # 게임 종료
# game_over()

# Quiz) 부동산 프로그램을 작성하시오

# (출력 예제)
# 강남 아파트 매매 : 10억 2010년
# 마포 오피스텔 전세 : 5억 2007년
# 송파 빌라 월세 500/50 2000년


# [코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, dea1_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.dea1_type = dea1_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(
            self.location,
            self.house_type,
            self.dea1_type,
            ":",
            self.price,
            self.completion_year,
        )


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
