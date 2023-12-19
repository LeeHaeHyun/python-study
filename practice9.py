# 클래스

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank_damage)

# 유닛이 수십 수백이 될 수 있는데 매번 이렇게 생성하면 비효율, 틀을 만드는게 클래스(붕어빵 틀)


# 일반 유닛 클래스
class Unit:  # 클래스, 클래스명
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")  # move의 원래 정의
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # __init__ : 파이썬에서 사용하는 생성자, 자동으로 실행
# # self를 제외하고 매개변수가 일치해야 객체를 만들 수 있다..

# # 멤버 변수
# # 클래스 내에 정의된 변수

# # 레이스 : 공중유닛, 비행기, 클로킹 (상대방에서 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True  # 클래스의 외부에서 변수에 의해 확장으로 사용할 수 있다.

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


# 메소드 파트
# 공격 유닛 클래스
class Attackunit(Unit):  # () 안에 클래스명을 넣으면 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # 자바의 super과 같음, 물려받을 내용
        self.damage = damage

    def attack(self, location):  # self는 자기 자신을 의미, 메소드 앞엔 반드시 self를 적어준다
        print(
            "{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
                self.name, location, self.damage
            )
        )

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# # 파이어뱃 : 공격유닛, 화염 방사기
# firebat1 = Attackunit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속 : 일치하는 것은 상속관계에 둘 수 있다.
# class Attackunit(Unit):  # () 안에 클래스명을 넣으면 상속    def __init__(self, name, hp, damage):
# Unit.__init__(self, name, hp)  # 자바의 super과 같음, 물려받을 내용
# self.damage = damage

# 다중 상속
# class Unit : 부모 클래스(상속을 물려줌) / class Attackunit : 자식 클래스(상속을 받음)

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 x


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
        )


# 공중 공격 유닛 클래스
class FlyableAttackUnit(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):  # 실행하기 위한 조건
        Attackunit.__init__(self, name, hp, 0, damage)  # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # unit의 move를 재정의: 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 결과:
# AttackUnit은 Unit 클래스를 상속받았고
# FlyableAttackUnit은 Flyable과 Attackunit 2개의 클래스를 다중 상속 받았다.

# 메소드 오버라이딩 : 자식 클래스에서 메소드를 쓰고 싶을 때

# 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = Attackunit("벌쳐", 80, 10, 20)  # attackunit 메소드를 호출했기에

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)  # flyableAttackUnit 메소드를 호출했기에

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


# pass
# 건물을 만든다
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass  # 그냥 넘어감, 없으면 오류남

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     pass  # 그냥 넘어감, 없으면 오류남


# game_start()
# game_over()


# super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(
            name, hp, 0
        )  # super은 ()를 써줘야 하고 self를 빼야 한다. 그리고 다중상속을 쓸 땐 쓰면 안된다.
        self.location = location
