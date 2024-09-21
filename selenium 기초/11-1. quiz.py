# 네이버 부동산에서 `송파 헬리오시티` 검색 후 목록 추출하기
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
url = "https://new.land.naver.com/"
browser.get(url)
time.sleep(1)

# 송파 헬리오시티로 이동 후 목록이 로딩될동안 대기.
items = browser.find_element(By.ID, "search_input")
items.send_keys("송파 헬리오시티")
items.send_keys(Keys.ENTER)
time.sleep(2)

# 거래방식 / 전체 면적 / 전체 동
items = browser.find_elements(By.XPATH, '//button[@class="list_filter_btn"]')[0].click()
time.sleep(2)
# 거래방식 (default : 매매) > 전체로 변경.
items = browser.find_element(By.XPATH, '//label[@for="complex_article_trad_type_filter_0"]').click()
time.sleep(1)
# 닫기 선택
items = browser.find_element(By.XPATH, '//button[@class="btn_close_panel"]').click()
time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")
# 검색결과 화면을 quiz.html 로 저장함.
with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

# 매물 전체 가져옴.
items = soup.find_all("div",attrs= {"class":"item_inner"})

for n,item in enumerate(items,1):
    # 동수 가져오가
    dong = item.find("span", attrs = {"class":"text"}).get_text().replace("헬리오시티","").strip()
    # 매매타입 / 가격 가져오기
    temp = item.find("div", attrs = {"class":"price_line"}).find_all("span")
    trace_type = temp[0].get_text()
    price = temp[1].get_text()
    # 면적 / 층수 가져오기
    temp = item.find("div", attrs = {"class":"info_area"}).find_all("p")[0].span.get_text()
    size = temp[temp.find("/")+1:temp.find("²")+1]
    floors = temp[temp.find("/",temp.find("²"))+1:temp.find("층")+1]

    print("========== 매물 {} ==========".format(n))
    print("거래 : {}".format(trace_type))
    print("면적 : {}".format(size))
    print("가격 : {}".format(price))
    print("동 : {}".format(dong))
    print("층 : {}".format(floors))
