# 터미널 python -m venv myenv
# .\myenv\Scripts\activate #액티베이트화
# pip install pandas, selenium, lxml
# pip install chromedriver-autoinstaller

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# 터미널 python 엔터 : 작업시작
# 복사 후 터미널에서 우클릭하면 달라붙는다.
# import~ BY까지 3줄을 터미널에 붙여넣고 아래 Chrome() 까지 실행

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화 하는 방법

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 2. 조회 항목 초기화(체크항목 해제) f12 개발자모드에서 체크박스를 선택하면 확인 가능
# input 박스에 name=fieldIds 개발자모드확인
# 체크박스 이름이 fieldIds인 것들을 찾아서 가져온다.
checkboxes = browser.find_elements(By.NAME, "fieldIds")

for checkbox in checkboxes:
    if checkbox.is_selected():  # 체크된 상태라면?
        checkbox.click()  # 골라서 클릭 (체크해제)

# 3. 조회 항목을 설정 (원하는 항목: 최대 6개까지 가능)
# (억)으로 화면이 보이지만 다른 영역으로 개발자모드에서 확인가능
items_to_select = ["시가", "고가", "저가"]

# input 필드 밑에 있는 label 영역을 가져오기 위해 부모인 td를 먼저 찾는다.
# input과 label이 형제 관계이기에 부모 - label을 찾는다.
for checkbox in checkboxes:
    # 부모 엘리먼트를 찾게 된다. 결과는 : td가 parent로 들어감
    parent = checkbox.find_element(By.XPATH, "..")
    # label이라는 태그 엘리먼트를 찾아서 label 변수에 넣는다.
    label = parent.find_element(By.TAG_NAME, "label")
    # print(label.text) # 체크박스 이름 목록을 확인하기 위해
    if label.text in items_to_select:  # 선택 항목
        checkbox.click()  # 리스트의 내용과 일치한다면 체크박스를 클릭해준다.

# 4. 적용하기
# 버튼을 보면 a태그의 href 속성에 아래와 같은 함수를 호출하는것을 확인
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 40):  # 1이상 40 미만 페이지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url + str(idx))  # http:// ...+ page 1,2,3.. 반복문
    # 5. 데이터 추출(pandas) 판다스(pd)
    df = pd.read_html(browser.page_source)[1]
    # 터미널 len(df) 데이터가 몇개인지 확인 # 테이블 3개가 있다.
    # df[0], df[1], df[2] 검색해보면 필요한 테이블은 df[1]이므로 [1]을 붙여준다.
    # NaN이라고 데이터가 없는 것이 많이 보여서 정리가 필요
    # 터미널 df.head(10)

    # 개발자모드를 키면 tr이라고 3줄을 차지하고 있다.
    # how= all (줄 전체가 비어있다면 지워라), how=any (줄 일부가 비워져있다면 지워라)
    df.dropna(axis="index", how="all", inplace=True)  # row기준으로 삭제를 한다,
    # inplace=True 그 결과를 반영하기 위해 필수로 적어준다, 안적으면 반영안됨

    # 개발자모드에서 보면 td colspan='13'이라고 불필요한 Nan이 포함되어있다.
    df.dropna(axis="columns", how="all", inplace=True)  # colum 기준으로 삭제를 한다.
    if len(df) == 0:  # 더이상 가져올 데이터가 없다면? 탈출
        break

    # 6. 파일저장 : 1페이지에서 저장, 2페이지에서 저장... 반복
    # 1페이지에서는 카테고리 헤더를 넣고 2페이지에서는 그대로 데이터만 넣는다.
    f_name = "sise.csv"
    if os.path.exists(f_name):  # 파일이 있다면?
        # CSV로 저장, 인코딩 UTF로 하고 앞에 1~13 번호는 삭제, 2페이지부터는 그대로 데이터만 append한다.
        df.to_csv(f_name, encoding="utf-8-sig", index=False, mode="a", header=False)
    else:  # 파일이 없다면? mode를 안적으면 w (쓰기 모드, 헤더값은 기본 true)
        df.to_csv(f_name, encoding="utf-8-sig", index=False)
    print(f"{idx} 페이지 완료")  # (idx에 관련 페이지를 넣는다)

    # exit(), 파이썬 종료하고 기본 터미널로 옴

browser.quit()
