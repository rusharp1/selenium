from bs4 import BeautifulSoup
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
# headless 즉, 창을 띄우지않고 랜더링을 통해 크롤링 가능
# 다만 해당의 경우, user-agent가 headless로 인식되어 몇몇 사이트에서 막을 수 있다.
options.headless = True
options.add_argument("window-size=1920x1080")
# 아래와 같이 user-agent를 나와 같은 상태로 만들 수 있음.
options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options= options)
url = "https://play.google.com/store/games"
browser.get(url)

time.sleep(1)

browser.execute_script("window.scrollTo(0,1080)")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

interval = 2
pre_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if pre_height == curr_height:
        break
    pre_height = curr_height

print("스크롤 완료")

# 창이 없기 때문에 잘 작동하는지 확인하기 어렵다.
# 이럴 때 아래와 같이 스크린샷 파일로 현재 상태를 저장할 수 있음.
browser.get_screenshot_as_file("google_game.png")

soup = BeautifulSoup(browser.page_source, "lxml")