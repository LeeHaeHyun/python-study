class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")


# 모듈 직접 실행
# 여기서 실행하는건지, 외부에서 호출하는건지를 구분할 수 있다.
if __name__ == "__main__":  # 여기서 바로 실행하면 아래 구문이 나온다.
    print("Vietnam 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("Vietnam 외부에서 모듈 호출")
