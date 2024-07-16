import time
import pytest
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from get_data_excel import search_get_excel_data
from select_element import select_element, select_elements
from selenium.webdriver.common.action_chains import ActionChains


# hotels.naver.com 에서 호텔을 검색합니다.

idx = 0

@pytest.fixture
def browser():
    url = "https://hotels.naver.com/"
    browser_instance = webdriver.Chrome()
    browser_instance.get(url)
    browser_instance.maximize_window()
    yield browser_instance
    browser_instance.close()

def bs4_setting(browser):
    return BeautifulSoup(browser.page_source , "lxml")

def test_select_location(browser, place): 
    select_element(browser, By.CLASS_NAME, "SearchBox_btn_location__AMvC8").click()
    # 지역명 입력
    select_element(browser, By.CLASS_NAME, "Autocomplete_txt__Ozp5b").send_keys(place)
    select_element(browser, By.XPATH, "//mark[contains(text(), '{}')]".format(place)).click()

def select_today_tomorrow(browser):
    ##################################### 1번째 방법 #####################################
    # 오늘 날짜와 일치하는 date 버튼 클릭, 다음날짜가 없는 경우, 다음달 1일 선택.
    # date = datetime.today()
    # start_date = select_element(browser, By.XPATH, "//b[contains(text(), '{}')]//ancestor::button".format(date.day))
    # start_date.click()
    # try:
    #     end_date =  select_element(browser, By.XPATH, "//b[contains(text(), '{}')]//ancestor::button".format(date.day + 1))
    # except:
    #     end_date = select_elements(browser, By.XPATH, "//b[text()='1']//ancestor::button")[1]
    # end_date.click()
    ##################################### 2번째 방법 #####################################
    # today.day 라는 class명을 가진 td 클릭.
    # today 라는 class 명윽 자니 td중 하위 button을 가지고있는 element 클릭
    start_date = select_element(browser, By.CSS_SELECTOR, "td.day.today")
    try:
        start_date.click()
    except:
        browser.execute_script("arguments[0].click();", start_date)
    end_date = select_element(browser, By.XPATH, "//td[@class='day']/button")
    try:
        end_date.click()  
    except:
        browser.execute_script("arguments[0].click();", end_date)

def select_big_browser_date(browser, date_value, one_year_later_str):
    global idx
    while True:
        # 달력 element를 찾은 뒤, yyyy.mm값을 추철함.
        # 
        calendar_list = select_elements(browser, By.CSS_SELECTOR, "div.sc-eqUAAy.czFkbX")
        calendar_list = [c.text.replace(" ", "") for c in calendar_list]
        # 설정한 date_list 값 중에 일치하는 값이 있는지 확인
        is_match = [date_value.startswith(cl) for cl in calendar_list]
        # 만약 모든 값이 False이면, 다음 버튼을 누르고 continue
        if not any(is_match):
            select_element(browser, By.CSS_SELECTOR, "button.sc-dcJsrY.sc-gsFSXq.imDkSH.glDkIk.next").click()
            idx+=1
            continue
        else:
            if one_year_later_str in calendar_list[1]:
                raise ValueError("일정을 찾을 수 없습니다.")
        # True가 있는 위치를 추출 후 day 클릭.
        calendar_month = select_elements(browser, By.CSS_SELECTOR, "div.sc-gEvEer.hMiJLh.month")[is_match.index(True)]
        calendar_day = select_element(calendar_month, By.XPATH, \
                                        ".//b[(text()='{}')]".format(str(int(date_value[8:])))).click()
        # 이전 버튼 idx번 누르기
        # //ancestor::button
        break

def test_select_checkin_checkout_dates(browser, date_list):
    global idx
    select_element(browser, By.CLASS_NAME, "SearchBox_btn_checkin__MdsBo").click()
    # 첫번째 날자가 두번째 날자보다 뒤일 때, 두 값을 스왑함.
    if datetime.strptime(date_list[0], "%Y.%m.%d") >  datetime.strptime(date_list[1], "%Y.%m.%d"):
        date_list[0], date_list[1] = date_list[1], date_list[0]
    # 달력이 2개만 있는 경우, 다음버튼을 눌러서 날짜를 찾는다.
    try:
        one_year_later = datetime.today() + timedelta(days=365)
        one_year_later_str = one_year_later.strftime('%Y.%m')
        idx+=1
        for _ in range(idx):
                select_element(browser, By.CSS_SELECTOR, "button.sc-dcJsrY.sc-iGgWBj.imDkSH.iWZXNz.prev").click()
                idx -=1
        for date_value in date_list:
            # 시작일, 종료일을 각각 선택함.
            select_big_browser_date(browser, date_value, one_year_later_str)
    # 달력이 3개 이상 있는 경우, 다음버튼을 누를 필요 없다.
    except:
        try:
            for date_value in date_list:
                actions = ActionChains(browser)
                # 달력 element를 찾은 뒤, yyyy.mm값을 추철함.
                calendar_list = select_elements(browser, By.CSS_SELECTOR, "div.sc-dAlyuH.cKxEnD")
                calendar_list = [c.text.replace(" ", "") for c in calendar_list]
                # 설정한 date_list 값 중에 일치하는 값이 있는지 확인 > error
                is_match = [date_value.startswith(cl) for cl in calendar_list]
                # 만약 모든 값이 False이면, 에러 발생시킴 > except 문으로 이동.
                if not any(is_match):
                    raise ValueError("is_match 리스트에는 적어도 하나의 True가 있어야 합니다.")
                calendar_month = select_elements(browser, By.CSS_SELECTOR, "div.sc-kpDqfm.DcnuU.month")[is_match.index(True)]
                calendar_day = select_element(calendar_month, By.XPATH, \
                                                ".//b[(text()='{}')]".format(str(int(date_value[8:]))))
                #  요소가 보이지 않거나 다른 요소가 겹쳐져 있는 상태에서 클릭하기 javascript 사용.
                try:
                    calendar_day.click()
                except:
                    browser.execute_script("arguments[0].click();", calendar_day)
                
        except:
            print("입력한 일정을 찾을 수 없습니다. 오늘~내일 일정으로 설정합니다.")
            for _ in range(idx):
                select_element(browser, By.CSS_SELECTOR, "button.sc-dcJsrY.sc-iGgWBj.imDkSH.iWZXNz.prev").click()
            select_today_tomorrow(browser)
    # 적용 버튼 선택
    select_element(browser, By.CLASS_NAME, "Calendar_sumbit__yuMvx").click()

def test_select_member(browser, target_value, kids_ages):
    select_element(browser, By.CLASS_NAME, "SearchBox_btn_people__kqLBO").click()
    # 현재 선택된 성인과 어린이 명수 가져오기
    current_values = select_elements(browser, By.CLASS_NAME, "SelectGuest_now__UOhjq")
    current_members = [
        int(current_values[0].text.replace("명", "")),  # 현재 성인 수
        int(current_values[1].text.replace("명", ""))   # 현재 어린이 수
    ]
    # 차이많큼 +, - 선택함.
    for i in range(2):
        differnce = target_value[i] - current_members[i]
        if differnce>0:
            button = select_elements(browser, By.CLASS_NAME, "SelectGuest_outer__Da2AQ")[i]
        elif differnce<0:
            button = select_elements(browser, By.CLASS_NAME, "SelectGuest_inner___xDpi")[i]
        else:
            # 변동이 없는 경우 다음루프로 이동.
            continue
        for _ in range(abs(differnce)):
            button.click()
    # 어린이 명수가 1명 이상일 때, 설정된 어린이 나이를 설정함
    if (target_value[1] > 0):
        for num, kids_ages_value in enumerate(kids_ages):
            select_elements(browser, By.XPATH, "//option[@value='{}']".format(kids_ages_value))[num].click()


def main():
    # chrome driver 를 사용하여 네이버 호텔 예약 페이지 이동
    url = "https://hotels.naver.com/"
    browser = webdriver.Chrome()
    browser.get(url)

    file_path = 'data_value.xlsx'
    excel_data_list = search_get_excel_data(file_path)
    for index, ed in enumerate(excel_data_list):
        try:
            place = ed[0]
            date_list = [ed[1], ed[2]]
            target_value = [ed[3], ed[4]]
            kids_ages = ed[5]
            # 
            print(f"====={index+1}=====")
            test_select_location(browser, place)
            print("위치 선택 완료")
            test_select_checkin_checkout_dates(browser, date_list)
            print("날짜 선택 완료")
            test_select_member(browser, target_value, kids_ages)
            print("인원 선택 완료")
            # 
            # 호텔 검색 클릭 (빈공간 한번 클릭 후 호텔 검색 선택)
            select_element(browser,By.CLASS_NAME , "SearchBox_search__0Suoj").click()
            select_element(browser,By.CLASS_NAME , "SearchBox_search__0Suoj").click()
            # 
            # 검색결과가 나올 때까지 기다림. 최대 2회.
            try:
                select_element(browser, By.CLASS_NAME, "SearchList_anchor__rS3VX")
            except:
                try:
                    select_element(browser, By.CLASS_NAME, "SearchList_anchor__rS3VX")
                except:
                    print("결과를 찾을 수 없습니다.")
            # 
            # 브라우저 뒤로가기 후 잠시 기다리기
            browser.back()
            select_element(browser, By.CLASS_NAME, "Footer_limitation__To1W3")
            time.sleep(1)
            print(f"{index+1}번째 값 테스트 성공했습니다.")
        except:
            print(f"{index+1}번째 값에 문제가 있습니다. 다시한 번 확인해주세요.")
    input

    
if __name__== "__main__":
   main()