import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from get_data_excel import filter_get_excel_data
from select_element import select_element, select_elements

# 성급 설정
def select_star(browser, star, filter_Value):
    try : 
        select_element(browser, By.XPATH, "//button[contains(text(),'{}')]". format(filter_Value)).click()
        for star_value in star:
            select_element(browser, By.XPATH, "//button[@class='Filter_CheckBox__LVGEx' and text()='{}']".format(star_value)).click()
    except:
        print(f"{filter_Value}값을 찾을 수 없습니다.")
# 가격 설정
def select_prices(browser, price, filter_Value):
    try:
        select_element(browser, By.XPATH, "//button[contains(text(),'{}')]". format(filter_Value)).click()
        price_value = []
        price_value.append(select_element(browser, By.ID, "price_min"))
        price_value.append(select_element(browser, By.ID, "price_max"))
        for idx, pv in enumerate(price_value):
            pv.clear()
            pv.send_keys(price[idx][0])
        select_element(browser, By.CLASS_NAME, "Rates_btn_apply__W7zcO").click()
    except:
        print(f"{filter_Value}값을 찾을 수 없습니다.")

# 숙박 유형 선택
def select_type(browser, types, filter_Value):
    try:
        select_element(browser, By.XPATH, "//button[contains(text(),'{}')]". format(filter_Value)).click()
        for type_value in types:
            select_element(browser, By.XPATH, "//button[@class='Filter_CheckBox__LVGEx' and text()='{}']".format(type_value)).click()
    except:
        print(f"{filter_Value}값을 찾을 수 없습니다.")


# 평점 선택
def select_grade(browser, grade, filter_Value):
    try:
        select_element(browser, By.XPATH, "//button[contains(text(),'{}')]". format(filter_Value)).click()
        for grade_value in grade:
            select_element(browser, By.XPATH, "//span[contains(text(),'{}점')]".format(grade_value)).click()
    except:
        print(f"{filter_Value}값을 찾을 수 없습니다.")

# 호텔 체인 선택
def select_chain(browser, chain, filter_Value):
    try:
        select_element(browser, By.XPATH, "//button[contains(text(),'{}')]". format(filter_Value)).click()
        for chain_value in chain:
            select_element(browser, By.XPATH, "//button[contains(text(),'{}')]".format(chain_value)).click()
    except:
        print(f"{filter_Value}값을 찾을 수 없습니다.")

# 주요시설 선택
def select_facility(browser, facility, filter_Value):
    try:
        select_element(browser, By.XPATH, "//button[contains(text(),'{}')]". format(filter_Value)).click()
        for facility_value in facility:
            select_element(browser, By.XPATH, "//button[text()='{}']".format(facility_value)).click()
    except:
        print(f"{filter_Value}값을 찾을 수 없습니다.")

def hotel_naver_filtering(browser, excel_data_list):
    filter_list = ['성급', '가격', '숙박유형', '평점', '호텔체인' , '주요시설']
    # 
    star = excel_data_list[0]            # 성급
    price = [excel_data_list[1], excel_data_list[2]]  # 최저가격, 최고가격
    types = excel_data_list[3]            # 숙박 유형
    grade = excel_data_list[4]           # 평점
    chain = excel_data_list[5]           # 호텔 체인
    facility = excel_data_list[6]        # 주요 시설
    # 
    select_star(browser, star, filter_list[0])
    select_prices(browser, price, filter_list[1])
    select_type(browser, types, filter_list[2])
    select_grade(browser, grade, filter_list[3])
    select_chain(browser, chain, filter_list[4])
    select_facility(browser, facility, filter_list[5])

if __name__== "__main__":
    url = "https://hotels.naver.com/places/KR1000073?checkIn=2024-07-28&checkOut=2024-07-30&adultCnt=2&childAges="
    browser = webdriver.Chrome()
    browser.get(url)
    file_path = r"selenium\naver 숙소예약 자동화\data_value.xlsx"
    excel_data_list = filter_get_excel_data(file_path)
    
    hotel_naver_filtering(browser, excel_data_list[0])