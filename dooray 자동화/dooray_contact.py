from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


def bs4_setting():
    return BeautifulSoup(browser.page_source, "lxml")

def wait_until(xpath_str):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located\
                                     ((By.XPATH, xpath_str)))
        return browser.find_element(By.XPATH,xpath_str)
    except:
        print("해당 element를 찾을 수 없습니다. 다시 한번 확인해주세요")
        print(xpath_str)
        sys.exit()

def wait_until_list(xpath_str):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located\
                                     ((By.XPATH, xpath_str)))
        return browser.find_elements(By.XPATH,xpath_str)
    except:
        print("해당 element를 찾을 수 없습니다. 다시 한번 확인해주세요")
        print(xpath_str)
        sys.exit()

# 리뉴얼로 이동하기
def go_to_renewal():
    ######### 리뉴얼 페이지로 이동하기 #########
    # 화면을 키워 설정 아이콘 노출하게끔 하기.
    browser.maximize_window()
    # 설정 선택하기
    wait_until("//span[@class='v2-icons-setting-white']").click()

    renewal = wait_until_list("//a[@role = 'menuitem']")
    renewal[-1].click()

    # 브라우저 탭 이동하기
    # 브라우저 tab list 살펴보기
    browser.window_handles
    # 2번째 탭을 last_tab으로 지정함.
    last_tab = browser.window_handles[1]
    # 2번째 탭으로 이동함.
    browser.switch_to.window(window_name=last_tab)

def open_lnb():
    time.sleep(1)
    list_check = browser.find_elements(By.XPATH,'//button[contains(@class, "css-1na46mx")]')
    if len(list_check) > 0:
        list_check[0].click()

# 새 연락처 생성하기
def make_new_contact():
    open_lnb()
    cnt = -1
    while cnt <1:
        cnt = int(input("몇 개의 연락처를 생성할지 입력해주세요."))
    for num in range(int(cnt)):
        # lnb에서 새 연락처 버튼 선택하기
        wait_until('//span[text()="새 연락처"]').click()

        # 새 연락처 내 더보기 클릭
        wait_until('//button[@class="css-1fy1wqq"]').click()

        # placeholder값 추출하기
        soup = bs4_setting()
        placeholder = soup.find_all("input", {"class":"css-tg3c7n"})
        placeholder = [placeholder[i]['placeholder'] for i in range(len(placeholder))]
        placeholder.pop(0)

        # placeholder과 같은 값 입력하기
        # email, 전화번호, url의 경우, 양식에 맞게 직접 텍스트 입력하기.
        contact_elem = browser.find_elements(By.XPATH, '//div[@class="css-djtklz"]//input[@class="css-tg3c7n"]')
        for i in range(len(contact_elem)):
            contact_elem[i].send_keys(placeholder[i]+str(num))

        # 양식과 틀린값 입력
        plc = ["이메일", "전화번호", "URL"]
        value = ["test"+str(num)+"@test.test", "000-000-00"+str(num), "test"+str(num)+".test.test"]
        for i in range(len(plc)):
            browser.find_element(By.XPATH, f'//input[@placeholder="{plc[i]}"]').send_keys(Keys.CONTROL+"a")
            browser.find_element(By.XPATH, f'//input[@placeholder="{plc[i]}"]').send_keys(value[i])
        
        # 생일/기념일 값에 오늘날짜 입력.
        date_elem = browser.find_elements(By.XPATH, '//input[@placeholder="YYYY-MM-DD"]')
        for i in range(2):
            date_elem[i].click()
            browser.find_element(By.XPATH, '//button[@class="css-zsumrd"]').click()

        # 메모 값 입력.
        browser.find_element(By.XPATH, '//textarea[@class="css-n3rizq"]').send_keys("메모")

        # 저장 후 닫기
        browser.find_element(By.XPATH, '//span[text()="저장"]').click()
        wait_until('//span[text()="닫기"]')
        browser.find_element(By.XPATH, '//span[text()="닫기"]').click()

# 연락처 목록중 최상위부터 n개 선택하기
def select_contact():
    open_lnb()
    wait_until('//div[text() = "내 연락처"]')
    time.sleep(1)
    browser.find_element(By.XPATH, '//div[text() = "내 연락처"]').click()
    
    # 연락처 총 개수 확인
    try:
        # 이부분은 왜있는거지????????
        # wait_until('//div[@class="css-1pzmb1"]')
        contact_cnt = wait_until_list('//label[@class="css-1pkki1k"]')
    except:
        contact_cnt = [1]
        
    print(f"선택 가능한 연락처 총 개수 : {len(contact_cnt)-1}")
    time.sleep(1)
    if len(contact_cnt)<2:
        # 연락처가 없으면 그냥 함수 종료시킴.
        print("연락처 총 개수가 적어서 이동할 수 없습니다.")
        return False
    move_cnt = -1
    while not(0<move_cnt<len(contact_cnt)):
        move_cnt = int(input("선택할 연락처 개수 : "))
    for i in range(1, move_cnt+1):
        contact_cnt[i].click()
    return True

# 버튼 선택해서 누르기
# 0: 메일 보내기, 1: 삭제, 2: 그룹으로 복사, 3: 내보내기
def select_button(n):
    button = wait_until_list('//div[@class="css-1q2k2wr"]')
    button[n].click()
    
# 연락처에서 그룹 복사 후 그룹 추가
def copy_to_new_group():
    # 그룹 목록이 없으면 함수 종료해버림
    if not select_contact():
        return
    # 그룹으로 복사 선택
    select_button(2)

    # 그룹 추가 후 그룹명 입력 + 확인
    wait_until('//span[text() = "그룹 추가"]')
    soup = bs4_setting()
    group_name_list = soup.select("div.css-spgta6")
    group_name_list = [group_name_list[i].get_text() for i in range(len(group_name_list))]

    # 그룹명이 없는 그룹이 만들어질때까지 루프
    browser.find_element(By.XPATH, '//span[text() = "그룹 추가"]').click()
    n = 0
    group_name = "그룹명"+str(n)
    while group_name in group_name_list:
        n+=1
        group_name = group_name = "그룹명"+str(n)

    wait_until('//input[@placeholder="그룹명을 입력하세요."]').send_keys(group_name)
    # 그룹 추가 내 확인버튼 누르기
    wait_until('//div[text()="그룹 추가"]')
    
    browser.find_element(By.XPATH,'//input[@placeholder="그룹명을 입력하세요."]\
                         //ancestor::div[@class= "css-14uzyaf"]\
                         //button[@class = "css-ma7kib"]').click()
    # 뭘 기다리는거지?????????
    # wait_until('//div[@class="css-1v6c1h6"]//div')

    # 방금 추가한 그룹 선택 후 확인
    time.sleep(1)
    wait_until(f'//div[text()="{group_name}"]/preceding-sibling::div').click()
    wait_until('//span[text()="확인"]').click()
    time.sleep(1)
    wait_until('//span[text()="확인"]').click()

    # 복사되었는지 확인하기
    open_lnb()
    wait_until('//span[text() = "{}"]'.format(group_name)).click()

def  delete_contacts():
    # 선택된 연락처 목록이 없으면 함수 종료해버림
    if not select_contact():
        return
    # 삭제 선택
    select_button(1)

options = webdriver.ChromeOptions()
# # headless 즉, 창을 띄우지않고 랜더링을 통해 크롤링 가능
# 다만 해당의 경우, user-agent가 headless로 인식되어 몇몇 사이트에서 막을 수 있다.
# options.headless = True
# 화면에 아이콘을 띄우지못해 찾을수 없을때가있음. 윈도우사이즈 지정함으로써 해결
options.add_argument('--window-size=1920x1080')
browser = webdriver.Chrome(options= options)

url = "https://doorayqa.dooray.com/contacts"
browser.get(url)

# insert_id = input("id를 입력하세요 : ")
# insert_pw = input("pw를 입력하세요 : ")
insert_id = "jtest1"
insert_pw = "test123!"

######### 로그인 과정 #########
id = browser.find_elements(By.XPATH, "//span[@class='input-box']/input")
id[0].send_keys(insert_id)
id[1].send_keys(insert_pw)
id[1].send_keys(Keys.ENTER)

######### 리뉴얼 얼럿 닫기 ###########
url = "https://doorayqa.dooray.com/contacts"
browser.get(url)
wait_until('//button[@class="css-1ihu6zl"]').click()


######### 자동분류정책 대기 후 본문 크롤링 후 닫기 #########

# 자동분류정책 나올때까지 대기함

# if (insert_id == "jtest"):
#     wait_until( '//span[@class = "hide-text v2-icons-popup-x"]')

#     # 자동분류정책 본문 가져옴.
#     soup = bs4_setting()
#     auto_align = soup.find("div", attrs="modal-dialog")
    
#     # 자동분류정책 모달창 닫기
#     close = browser.find_element(By.XPATH, '//span[@class = "hide-text v2-icons-popup-x"]')
#     close.click()

######### 리뉴얼 페이지로 이동하기(이제 기본으로 리뉴얼로감) #########
# go_to_renewal()

# lnb가 닫혀있으면 lnb열기

check = {1:make_new_contact, 2:copy_to_new_group
         }
######## 원하는만큼 업무 등록 #########
insert = "1"
while 1:
    print("0. 종료")
    print("1. 새 연락처 만들기")
    print("2. 임의의 연락처 그룹으로 복사")
    
    insert = input("번호를 입력하세요 : ")
    if insert == "0":
        break
    check[int(insert)]()

######### 리뉴얼 페이지로 이동된 상태에서 원래 페이지로 이동 #########

# Legacy = browser.find_element(By.XPATH, "//div[@class = 'css-1dbddxm']")
# Legacy.click()

input("종료되었습니다.")