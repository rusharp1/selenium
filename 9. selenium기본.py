# 직접 웹브라우저를 컨트롤하여 webscraping
# 현재 버전에 맞는 chrome driver.exe파일 다운로드해야됨
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 현재 폴더에 있음 = ./, 적지 않아도 된다.
browser = webdriver.Chrome() #"./chromedriver.exe"
browser.get("https://naver.com")
# selenium 문법이 변경되었다.
# find_element_by_class_name 은 하단과 같이 명시되어야 함.
# 꼭 from selenium.webdriver.common.by import By 를 통해 by import
elem = browser.find_element(By.CLASS_NAME, "ico_naver")
browser.find_element()
elem.click() # 클릭
browser.back() # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침
elem.send_keys("나도코딩") # 텍스트 전송
# 아래를 위해서는 Keys를 import 해야한다.
elem.send_keys(Keys.ENTER) # ENTER 전송

# tag_name이 "a"인 element를 가져온다. (가장 첫번째)
elem = browser.find_element(By.TAG_NAME, "a") # TAG_NAME으로 찾아보기
# tag_name이 "a"인 element를 모두 가져온다.
elem = browser.find_elements(By.TAG_NAME, "a")

browser.get("http://daum.net")
elem = browser.find_element(By.NAME , "q") # NAME으로 찾아보기
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()
elem.send_keys("나도코딩") 
elem = browser.find_element(By.XPATH , '//*[@id="daumSearch"]\
                            /fieldset/div/div/button[3]') # XPATH로 찾아보기
elem.click()
# 현재 있는 탭만 닫음
browser.close()
# 브라우저 전체를 종료
browser.quit()