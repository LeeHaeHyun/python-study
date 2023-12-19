

# super은 다중상속에서 쓸 수 없다.
class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flayable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  # 다중 상속할 땐 super을 쓰면 안됨
        Unit.__init__(self)  # 다중 상속은 이렇게 쓴다.
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()  # 결과: Unit 생성자, // Flayable은 상속되지 않은 오류

# ★ super()는 맨처음의 클래스에 대해서만 호출이 된다. 다중상속이 안된다.
