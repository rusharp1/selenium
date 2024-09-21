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

# 대기하기
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
    # 화면을 키워 설정 아이콘 노출하기.
    browser.maximize_window()
    # 설정 선택하기
    renewal = wait_until("//span[@class='v2-icons-setting-white']")
    renewal.click()

    renewal = wait_until_list("//a[@role = 'menuitem']")
    renewal[-1].click()

    # 브라우저 탭 이동하기
    # 브라우저 tab list 살펴보기
    browser.window_handles
    # 2번째 탭을 last_tab으로 지정함.
    last_tab = browser.window_handles[1]
    # 2번째 탭으로 이동함.
    browser.switch_to.window(window_name=last_tab)

# 프로젝트 이동
def go_to_project():
# 프로젝트 리스트로 확대
    list_check = browser.find_elements(By.XPATH,"//button[contains(@class, 'css-1t268w2')]")
    if len(list_check) > 0:
        list_check[0].click()

    project_name = input("프로젝트명을 입력하세요(full name) : ")
    # `max` 프로젝트로 이동
    wait_until("//span[text() = '{}']".format(project_name)).click()

# 업무 생성
def make_task(): 
    go_to_project()
    # 업무추가버튼 누르기
    

    print("서버지연 등으로 입력 개수보다 적게 만들어질 수 있습니다.")
    print("원하는 업무 개수보다 조금 더 여유를 가지고 입력해주세요.")
    task_cnt = input("만들 업무 개수를 입력하세요 : ")
    task_cnt = int(task_cnt)
    print("예상 소요 시간 : {}분".format(task_cnt/50))

    wait_until("//div[@class = 'svg-icon css-1ytc7q1']").click()
    for i in range(0,task_cnt): # 업무 1000개 등록하기
        time.sleep(1)
        browser.find_element(By.XPATH,'//div[@class="ProseMirror ProseMirror-focused"]').send_keys(i)
        browser.find_element(By.XPATH,"//span[text() = '저장 후 계속 등록']").click()

# 업무 설정으로 이동 후 탭 이동
# 0 : 일반, 1: 대시보드, 2:업무, 3:드라이브 4:위키, 5:포트폴리오
def goto_settings(n):
    go_to_project()
    # 설정 클릭
wait_until('//div[@class="svg-icon css-195zilh"]').click()

# 프로젝트 설정, 멤버그룹 설정, 초대하기, url 복사, 즐겨찾는 프로젝트에 제거, 나가기 순서

settings = wait_until_list('//div[@class="css-13w8m0v"]')
settings[0].click()

# 타이틀바 텍스트 가져오기.
wait_until("//button[@data-testid = 'tab-button']")
soup = bs4_setting()
soup.find_all("button", {"data-testid" : "tab-button"})
# soup.find_all("button", {"class":"css-1lnpnlk"})
# soup.select("button.css-1lnpnlk")

# 설정 (일반, 대시보드, 업무, 드라이브, 위키)
# ` css-1lnpnlk` 가 class명에 포함되어있는 모든 button 찾기 -> contains

setting_list = wait_until_list('//button[contains(@class, " css-1isdoaq")]')
# 설정 > 업무로 이동
setting_list[2].click()

######### 프로젝트 메일 10개 추가 #########
def make_task_mail():
    goto_settings(2)

    # 메일 주소로 이동
    
    wait_until('//li[text()="메일 주소"]').click()
    time.sleep(1)
    mail_list = browser.find_elements(By.XPATH, '//tbody[@class="css-1al21c4"]/tr')
    cnt = len(mail_list)
    num = 0
    while cnt < 10:
        # 메일 연동 클릭
        wait_until('//span[text()="메일 주소 생성"]').click()
        mail_add = browser.find_elements(By.XPATH, '//div[@class="css-1sffydw"]/div/div/input')
        # 메일 주소 / 메일 이름 입력
        mail_add[0].send_keys(str(num))
        mail_add[1].send_keys(str(num))
        browser.find_element(By.XPATH, '//span[text() = "확인"]').click()

        time.sleep(1)

        # 접미사/접두사 얼럿 확인하기
        soup = bs4_setting()
        alert = soup.select("span.css-158icaa")
        if alert:
            alert_text = alert[0].get_text()
            alert_text = alert_text[:alert_text.find("가")]
            if '접미사' in alert[0].get_text():
                # claer()하니까 이전값이랑 다음값이 겹쳐서 노출됨
                mail_add[0].send_keys(Keys.CONTROL+'a')
                mail_add[0].send_keys(str(num)+alert_text)

            browser.find_element(By.XPATH, '//span[text() = "확인"]').click()
        num = num+1
        # 얼럿 나오는지 확인
        '//div[@class="input-wrapper css-ph97dh"]/div/input'
        time.sleep(2)
        alert = browser.find_elements(By.XPATH, '//div[@class="css-4wlfcn"]')
        if alert:
            soup = bs4_setting()
            alert_text = soup.find("div", {"class" : "css-198rcoj"})
            print (alert_text.get_text())
            browser.find_element(By.XPATH, '//span[text() = "확인"]').click()
            continue
        cnt +=1

    browser.find_element(By.XPATH, '//button[@class="close-dialog css-58wyhh"]').click()

######### 업무 태그 추가 #########
def make_task_tag():
    goto_settings(2)

    wait_until('//li[text()="태그"]').click()

    tag_categry = ["", "필수:","1개만:","필수+1개만:"]
    for i in range(3):
        for category in tag_categry:
            # 그룹없는 태그 추가
            browser.find_element(By.XPATH,'//span[text()="태그 추가"]').click() 
            tag_add = wait_until('//div[@class = "input-wrapper css-1kjmqkl"]/div/input')
            tag_add.send_keys(category+str(i))
            time.sleep(0.5)
            tag_add.send_keys(Keys.ENTER)
            time.sleep(0.5)
    
    checkbox = browser.find_elements(By.XPATH, '//div[@class="css-ckvlh"]//div[@class="css-1ntjw8x etmda960"]')
    checkbox[1].click()
    checkbox[2].click()
    checkbox[4].click()
    checkbox[5].click()
    browser.find_element(By.XPATH, '//button[@class="close-dialog css-58wyhh"]').click()
    

######### 업무 마일스톤 추가 #########
def make_task_mileston():
    goto_settings(2)

    wait_until('//li[text()="단계"]').click()

    # 기간 있음으로 5개 생성
    for i  in range(5):
        wait_until('//span[text() = "단계 추가"]').click()
        time.sleep(1)
        # 시작날짜, 종료날짜 텍스트 가져오기
        soup = BeautifulSoup(browser.page_source, "lxml")
        soup.select("div.input-wrapper.css-zxomol")[0].select("input")
        start_day = soup.select("div.input-wrapper.css-zxomol")[0].select_one("input")['value']
        end_day = soup.select("div.input-wrapper.css-zxomol")[1].select_one("input")['value']
        start_day = start_day[5:].replace("-","")
        end_day = end_day[5:].replace("-","")
        
        # 시작날짜-종료날짜 로 마일스톤 생성.
        wait_until("//div[@class = 'input-wrapper css-1axan4x']")
        browser.find_element(By.XPATH, "//div[@class = 'input-wrapper css-1axan4x']/div/input").send_keys(start_day,"-", end_day)
        browser.find_element(By.XPATH, "//span[text() = '추가']").click()
    # 기간 없음 / 종료로 각각 5개 생성
    text = ["기간없음", "종료"]
    for i  in range(5):
        for t in text:
            wait_until('//span[text() = "단계 추가"]').click()
            wait_until('//span[@class="radio-custom"]').click()
            wait_until("//div[@class = 'input-wrapper css-1axan4x']")
            browser.find_element(By.XPATH, "//div[@class = 'input-wrapper css-1axan4x']/div/input").send_keys(t,i)
            browser.find_element(By.XPATH, "//span[text() = '추가']").click()
    
    # 종료가 제목에 포함된 마일스톤을 다 종료로 변경
    wait_until('//li[@class = "css-1s9grls edskt4q0"]')
    milestones_txt = browser.find_elements(By.XPATH,'//div[@class="css-ooqh6p"]/span[1]')
    milestones_bt = browser.find_elements(By.XPATH,'//div[@class="css-1qf3h2m"]//span[text() = "종료"]')

    for i in range(len(milestones_txt)):
        if "종료" in milestones_txt[i].text:
            milestones_bt[i].click()
            time.sleep(1)

        browser.find_element(By.XPATH, '//button[@class="close-dialog css-58wyhh"]').click()

######### 업무 + 댓글 추가 #########
def make_task_comment():

    # 업무로 이동 후 새 업무 작성 (title : 댓글 업무)
    go_to_project()
    wait_until("//div[@class = 'svg-icon css-1ytc7q1']").click()
    time.sleep(1)
    wait_until('//div[@class="ProseMirror ProseMirror-focused"]').send_keys("댓글 업무")
    wait_until("//span[text() = '저장']").click()
    time.sleep(1)
    
    # `댓글 업무` 업무로 이동
    wait_until( '//div[text()="댓글 업무"]').click()
    wait_until('//span[@class="placeholder ProseMirror-widget"]').click()
    for i in range(20):
        wait_until('//div[@class="ProseMirror ProseMirror-focused"]').send_keys(str(i))
        time.sleep(1)
        wait_until_list('//button[@class="css-1tya6nd"]')[1].click()


options = webdriver.ChromeOptions()
# # headless 즉, 창을 띄우지않고 랜더링을 통해 크롤링 가능
# 다만 해당의 경우, user-agent가 headless로 인식되어 몇몇 사이트에서 막을 수 있다.
# options.headless = True
# 화면에 아이콘을 띄우지못해 찾을수 없을때가있음. 윈도우사이즈 지정함으로써 해결
options.add_argument('--window-size=1920x1080')
browser = webdriver.Chrome(options= options)

url = "https://doorayqa.dooray.com/task"
browser.get(url)

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

wait_until('//button[@class="css-1ihu6zl"]')
browser.find_element(By.XPATH, '//button[@class="css-1ihu6zl"]/span').click()
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


check = {1:make_task, 2:make_task_mail,\
         3:make_task_tag, 4:make_task_mileston,\
         5:make_task_comment
         }
######### 원하는만큼 업무 등록 #########
insert = "1"
while 1:
    print("0. 종료")
    print("1. 프로젝트 업무 만들기")
    print("2. 프로젝트 업무 메일 만들기 (10게)")
    print("3. 프로젝트 태그 만들기")
    print("4. 프로젝트 마일스톤 만들기")
    print("5. 프로젝트 업무 + 댓글 20개 작성")
    
    insert = input("번호를 입력하세요 : ")
    if insert == "0":
        break
    check[int(insert)]()

######### 리뉴얼 페이지로 이동된 상태에서 원래 페이지로 이동 #########

Legacy = browser.find_element(By.XPATH, "//div[@class = 'css-1dbddxm']")
Legacy.click()

input("종료되었습니다.")