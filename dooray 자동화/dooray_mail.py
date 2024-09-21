from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import sys

def bs4_setting():
    return BeautifulSoup(browser.page_source, "lxml")

# 대기하기
def wait_until(xpath_str):
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located\
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

    log = '//div[contains(@class,"ProseMirror")]'
    for temp in range(59,500):
        time.sleep(1)
        browser.find_element(By.XPATH,log).send_keys(temp)
        browser.find_element(By.XPATH,'//div[@class="css-g8slxl"]/button').click() 


def open_lnb():
    time.sleep(1)
    list_check = browser.find_elements(By.XPATH,'//button[contains(@class, "css-1na46mx")]')
    if len(list_check) > 0:
        list_check[0].click()

######### 내부 사용자에게 메일 전송하기 #########
def send_mail():
    open_lnb()
    # 새 메일 선택 후 해당 탭으로 포커싱
    wait_until('//span[text()="새 메일"]').click()
    browser.window_handles
    last_tab = browser.window_handles[1]
    browser.switch_to.window(window_name=last_tab)

    # 받는 사람, 참조, 제목 순서
    new_mail_textbox = wait_until_list('//input[@class="css-tg3c7n"]')
    while(1):
        id = input("받는 사람 id를 입력해주세요(종료는 엔터키) : ")
        if (len(id) == 0):
            break
        new_mail_textbox[0].send_keys("{}@doorayqa.dooray.com;".format(id))
    while(1):
        title = input("제목을 입력해주세요 : ")
        if (len(title) > 0):
            new_mail_textbox[2].send_keys(title)
            break
    time.sleep(1)
    FTC_val  = {}
    soup = bs4_setting()
    # 보낸 사람, 받는 사람, 참조, 숨은 참조, 제목 (숨은참조 및 보낸사람 노출여부 체크 필요)
    row_val = soup.select("div.row")
    temp = 0
    # 보낸 사람 입력 (노출되어있지 않으면 노출되지 않게)
    if "보낸" in row_val[0].select_one("div.label").text:
        FTC_val[row_val[0].select_one("div.label").text] =\
                [row_val[0].select_one("div.input-email").text,row_val[0].select_one("div.input-name").text]
        temp+=1
    # To, Cc, Bcc 입력
    for i in range(temp, len(row_val)-2):
        mail_list = row_val[i].select("div.css-ccte1h")
        mail_list = [ml.text for ml in mail_list]
        FTC_val[row_val[i].select_one("div.label").text] =\
            mail_list
    # 제목값 입력
    FTC_val["제목"] = row_val[len(row_val)-2].select_one("input.css-tg3c7n")['value']
    
    # 출력
    for ftc_k, ftc_v in FTC_val.items():
        print(ftc_k, " : ", ftc_v)

    temp = len(browser.window_handles)
    # 전송 누르기
    new_mail_textbox[0].send_keys(Keys.CONTROL+Keys.ENTER)
    while(1):
        try:
            # 얼럿이 나오면 얼럿 텍스트 출력 후 확인 누름
            time.sleep(1)
            soup = bs4_setting()
            print("얼럿 내용 : ",soup.select_one("div.css-14uzyaf").select_one("div.focusSection").div.text)
            browser.find_element(By.XPATH, '//button[@class="css-ma7kib"]').click()
            time.sleep(5)
        except:
            time.sleep(2)
            # 기존 창과 이후 창이 같은 경우, 전송 실패 안내문구 노출
            if temp == len(browser.window_handles):
                print("메일 전송 실패하였습니다. 얼럿을 확인해주세요.")
            else:
                print("메일 전송 성공하였습니다.")
            break
    # 기존 창으로 이동하기.
    browser.window_handles
    last_tab = browser.window_handles[0]
    browser.switch_to.window(window_name=last_tab)

######### 폴더가 있는 사용자인지 체크하기 #########
def check_folder():
    # LNB 열기
    open_lnb()
    # LNB 메일함 목록 가져오기 (텍스트)
    soup = bs4_setting()
    bs4_mail_list = soup.find_all("div", attrs="css-b3950k")
    bs4_mail_list = [bml.get_text() for bml in bs4_mail_list]

    # 맨 마지막에 공용메일이 있는지 확인 (무조건 새 메일 버튼 뒤에 나오기)
    Public_mail = 0
    if bs4_mail_list[-1] == "공용 메일":
        Public_mail = 1
    # 폴더가 있는지 체크해야됨
    trash_idx = bs4_mail_list.index("휴지통")
    # 공용 메일이 있는 테넌트 : 공용메일을 포함하여 휴지통 이후 list가 3개 이상이어야 함 (새 폴더 버튼, 공용 메일 버튼)
    # 공용 메일이 없는 테넌트 : 공용메일을 제외하고 휴지통 이후 list가 2개 이상이어야 함 (새 폴더 버튼)
    # 공용 메일 개수 : bs4_mail_list.count("공용 메일")) = 1
    if (len(bs4_mail_list)-trash_idx- Public_mail) >=3:
        print("폴더가 있는 사용자")
        trash_idx +=1

    # lnb 다시 닫기
    wait_until('//div[@class="svg-icon css-8dpcvj"]').click()
    return trash_idx


######### 메일 목록 타이틀바 버튼 가져오기 #########
def mail_list_title_bar():
    trash_idx = check_folder()

    print("메일 목록 타이틀바 버튼")
    # 딕셔너리 선언
    title_bar_list = {}
    # LNB상단부터 폴더까지 열기
    for i in range(trash_idx+1):     
        # LNB 열기
        open_lnb()

        # 메일함 선택
        mail_list=wait_until_list('//div[@class="css-b3950k"]') 
        mail_list[i].click()

        # 로딩 기다리기, 10초까지
        browser.implicitly_wait(10)
        
        # 상단바 내 더보기 메뉴 여부 체크 & 더보기 있으면 클릭
        more_button = browser.find_elements(By.XPATH, \
                        '//div[@class="css-1pagc1b"]//div[contains(@class,"css-1mcsp7l")]')
        if len(more_button)>0:
            more_button[0].click()
        soup = bs4_setting()
        # 메일함명 가져오기
        title_bar_name = soup.select_one("div.css-9qd35h").get_text()
        # 메일함 상단 버튼목록 가져오기
        title_bar = soup.select("div.css-1pagc1b>div")

        title_bar = [tb_name.get_text().strip() for tb_name in title_bar]
        title_bar_list[title_bar_name] = title_bar

    for tbl, tblv in title_bar_list.items():                  
        print(tbl, tblv)

######### 메일 상세보기 타이틀바 버튼 가져오기 #########
def mail_contents_title_bar():
    trash_idx = check_folder()
    print("메일 상세보기 타이틀바 버튼")
    
    view_types = [["분할 뷰", "대화형"], ["분할 뷰", "시간순"],\
                 ["목록 뷰", "대화형"] , ["목록 뷰", "시간순"]]
    
    # 뷰 타입 초반 변경을 위한 메일함 이동

    for view_type in view_types:
        # 딕셔너리 선언
        open_lnb()
        wait_until('//span[text() = "받은 메일함"]').click()
        title_bar_list = {}
        # 분할 뷰 / 시간 순으로 세팅함
        wait_until('//div[@class = "css-zoxwqk"]//div[@class="css-1miwjnc"]').click()
        wait_until(f'//span[text() = "{view_type[0]}"]').click()
        wait_until('//div[@class = "css-zoxwqk"]//div[@class="css-1miwjnc"]').click()
        wait_until(f'//span[text() = "{view_type[1]}"]').click()
        # 받은 메일함부터 폴더까지 열기
        for i in range(4, trash_idx+1):
            # LNB 열기
            open_lnb()
            mail_list=wait_until_list('//div[@class="css-b3950k"]')
            # 메일함 선택함.
            # element click intercepted 에러 : Keys.ENTER 전송으로 해결
            mail_list[i].click()
            time.sleep(1)
            
            soup = bs4_setting()
            # 메일함 제목 가져오기
            title_bar_name = soup.select_one("div.css-9qd35h").get_text()

            # 목록이 나올때까지 최대 10초까지 대기
            # 제목이 나오지 않으면 메일이 없는 얼럿 노출.
            try : 
                WebDriverWait(browser, 10).until(EC.presence_of_element_located\
                                        ((By.XPATH, '//div[contains(@class,"css-13wylk3")]')))
            except:
                print("* ",title_bar_name,": 메일이 없어 확인이 불가능합니다.")
                title_bar_list[title_bar_name] = ["알 수 없음"]
                continue

            soup = bs4_setting()
            # 메일함 제목 가져오기
            title_bar_name = soup.select_one("div.css-9qd35h").get_text()
            
            # 메일 클릭하여 메일 상세보기 체크
            list_in_mail = browser.find_elements(By.XPATH,'//div[@class="css-zz1tso"]')
            list_in_mail[1].click()
            
            if(title_bar_name.find("스팸") != -1):
                wait_until('//span[text() = "확인"]').click()
            # 상단바 내 더보기 메뉴 여부 체크 & 더보기 있으면 클릭
            browser.implicitly_wait(10)
            more_button = browser.find_elements(By.XPATH, \
                            '//div[@class="css-44gx6g"]//div[contains(@class,"css-1mcsp7l")]')
            if len(more_button)>0:
                try:
                    more_button[0].click()
                except:
                    temp = browser.find_element(By.XPATH,'//div[@class ="sash-line css-p4neir"]')
                    ActionChains(browser).drag_and_drop_by_offset(temp,-200,0).perform()
                    more_button[0].click()
            
            # 상세보기 타이틀바 버튼 목록 가져오기
            soup = bs4_setting()
            # 임시보관의 이어쓰기
            title_bar = soup.select("div.css-1ik8gfe>div.css-f9gn4h")
            # 타 메일함 상단바 버튼
            title_bar = title_bar + soup.select("div.css-1ik8gfe>div.css-9ncwx")
            # 더보기 내 버튼 목록
            title_bar = title_bar + soup.select("div.css-13w8m0v")
            title_bar = [tb_name.get_text().strip() for tb_name in title_bar]
            title_bar_list[title_bar_name] = title_bar
        print("=============================================================")
        print(f"뷰 타입 : {view_type[0]}&{view_type[1]}")
        for tbl, tblv in title_bar_list.items():                  
            print(tbl, tblv)

options = webdriver.ChromeOptions()
# # headless 즉, 창을 띄우지않고 랜더링을 통해 크롤링 가능
# 다만 해당의 경우, user-agent가 headless로 인식되어 몇몇 사이트에서 막을 수 있다.
# options.headless = True
# 화면에 아이콘을 띄우지못해 찾을수 없을때가있음. 윈도우사이즈 지정함으로써 해결
options.add_argument('--window-size=1920x1080')
browser = webdriver.Chrome(options= options)
url = "https://doorayqa.dooray.com/mail"
browser.get(url)
browser.maximize_window()
# insert_id = input("id를 입력하세요 : ")
# insert_pw = input("pw를 입력하세요 : ")
insert_id = "jtest"
insert_pw = "test123!"

######### 로그인 과정 #########
id = browser.find_elements(By.XPATH, "//span[@class='input-box']/input")
id[0].send_keys(insert_id)
id[1].send_keys(insert_pw)
id[1].send_keys(Keys.ENTER)

######### 리뉴얼 팝업 닫기 ###########
# 다른 서비스로 이동한 경우를 대비하여 다시한번 메일로 이동시킴
url = "https://doorayqa.dooray.com/mail"
browser.get(url)
wait_until('//button[@class="css-1ihu6zl"]').click()
wait_until('//span[@class = "css-1oteowz"]').click()
######### 자동분류정책 대기 후 본문 크롤링 후 닫기 #########

# # 자동분류정책 나올때까지 대기함
# if (insert_id == "jtest"):
#     wait_until( '//span[@class = "hide-text v2-icons-popup-x"]')

#     # 자동분류정책 본문 가져옴.
#     soup = bs4_setting()
#     auto_align = soup.find("div", attrs="modal-dialog")
    
#     # 자동분류정책 모달창 닫기
#     close = browser.find_element(By.XPATH, '//span[@class = "hide-text v2-icons-popup-x"]')
#     close.click()

######### 리뉴얼 페이지로 이동하기 #########

# go_to_renewal()


# LNB 메일함 버튼 변수 가져오기 (selenium)


check = {1:send_mail, 2:mail_list_title_bar,
         3:mail_contents_title_bar}

######### 원하는만큼 업무 등록 #########
insert = "0"
while 1:
    print("1. 메일 전송하기")
    print("2. 메일 목록 타이틀바 버튼 가져오기")
    print("3. 메일 상세보기 타이틀바 버튼 가져오기")
    
    insert = input("번호를 입력하세요 : ")
    if insert == "0":
        break
    check[int(insert)]()

######### 리뉴얼 페이지로 이동된 상태에서 원래 페이지로 이동 #########

# Legacy = browser.find_element(By.XPATH, "//div[@class = 'css-1dbddxm']")
# Legacy.click()

input("종료되었습니다.")