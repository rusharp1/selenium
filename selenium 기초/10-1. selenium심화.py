from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# webdriverWait을 사용하기 위한 import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()
browser.get("https://naver.com")
# 로그인 버튼을 클릭 후 이동
elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()

# id, pw 입력 레이아웃으로 이동 후 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

# 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

# 로딩을 위해 잠시 기다림
time.sleep(3)
browser.implicitly_wait(3)
# webDriverWait 을 통해 browser을 최대 10초동안 기다림 (10초가 넘어가면 에러)
# ID가 id 인 element를 찾으면 EC가 True를 리턴함.
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "id")))


# 새로운 id/pw입력을 위해 입력창을 초기화함
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("shop2930")

# html 정보 출력
print(browser.page_source)

browser.quit