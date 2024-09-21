from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriverWait을 사용하기 위한 import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_until(xpath_str):
    # 아래값이 나올때까지 기다림 ( 다만 나오지 않는 경우 최대 3초까지 기다림. )
    WebDriverWait(browser, 3).until(EC.presence_of_element_located\
        ((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window() # 크롬창을 최대로 키움
browser.get("https://flight.naver.com/")

# browser.implicitly_wait(3)
time.sleep(3)

# 처음나오는 광고 닫기 선택
elems = browser.find_elements(By.XPATH, '//button[@class="btn"]')
elems[1].click()

# 상위 button에서 하위의 2번째 버튼을 찾는다.
elems = browser.find_element(By.XPATH, '//div[@class="btns"]/button[1]')

# class="btn as_share naver-splugin spi_sns_share"
# class="jsx-1527821584 btn as_top"
# class="btn" 이렇게 3개의 class가 선택됨(왤까?)
# elems = browser.find_elements(By.CLASS_NAME, "btn")
# elems[3].click()

# // : html 전체중에서 찾겠다는 의미
# button 중에서 text 가 `가는 날`인 버튼 찾음.
time.sleep(1)
browser.find_element(By.XPATH, '//button[text() ="가는 날"]').click()

# 첫번째 27일~ 첫번째 30일 선택
wait_until('//b[text() = "27"]')
day = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day[0].click()
wait_until('//b[text() = "30"]')
day = browser.find_elements(By.XPATH, '//b[text() = "30"]')
day[0].click()

# 도착 클릭 > 국내 클릭 > 제주도 클릭
wait_until('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]').click()
wait_until('//button[text() = "국내"]')
browser.find_element(By.XPATH, '//button[text() = "국내"]').click()
# 텍스트에 `제주`를 포함하는 값을 클릭함 = contains(text(), "제주국제공항")
wait_until('//i[contains(text(), "제주국제공항")]')
browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]').click()


# wait_until('//spot[contains(text(), "항공권 검색")]')
browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]').click()

# div인데 class값이 dom~ 인 값을 찾을 때, @를 사용함.
# <div class="domestic_Flight__sK0eA result"> 를 찾음.
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located\
        ((By.XPATH, '//div[@class = "domestic_Flight__sK0eA result"]')))
print(elem.text)

input("종료하려면 enter을 입력하세요")
browser.quit()