# import theater_module # 모듈 임포트

# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조할인 영화 보러 감
# theater_module.price_soldier(5)  # 5명의 군인이 영화보러 감

# import theater_module as mv  # 별칭을 붙여 바꿀 수 있음

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *  # 모듈의 모든 것을 쓰겠다.

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning  # 모듈 안에서 메소드 일부만 불러올 수 있음

# price(5)
# price_morning(6)

# from theater_module import price_soldier as price  # 메소드 일부에도 별칭을 부를 수 있음

# price(5) # 군인 할인 가격에 대한 별칭

# 패키지 : 모듈들을 모아놓은 것
# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 메소드만 불러옴

# trip_to = ThailandPackage()
# trip_to.detail()

# __all__

# from travel import *

# trip_to = vietnam.VietnamPackage()  # init.py에서 사용할 공개할 파일을 따로 정확히 써주어야 한다.
# trip_to = thailland.ThailandPackage()  # init.py에서 공개하지 않아서 오류가 뜬다.
# trip_to.detail()

# 패키지, 모듈 위치
# import inspect
# import random

# print(inspect.getfile(random))  # 모듈의 위치가 어딘지 알려준다.
# print(inspect.getfile(vietnam))  # 모듈의 위치가 어딘지 알려준다.

# pip install : 패키지 설치하기
# 구글에서 pypi : beautifulsoup 웹 스크랩할 수 있는 패키지
# 터미널에 pip install types-beautifulsoup4 엔터

# from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# pip list : 현재 설치되어있는 패키지 내용
# pip show beautifulsoup4 : 이 패키지 정보
# pip install --upgrade beautifulsoup4 : 최신 버전으로 설치
# pip uninstall beautifulsoup4 : 패키지 삭제
