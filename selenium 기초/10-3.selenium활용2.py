from bs4 import BeautifulSoup
import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()
url = "https://play.google.com/store/games"
browser.get(url)

# 브라우저 로딩이 끝날때까지 기다림
time.sleep(1)

# 스크롤 내리기
# 윈도우에서 1080 위치로 스크롤을 내린다(모니터 해상도)
browser.execute_script("window.scrollTo(0,1080)")

# 화면 가장 아래로 스크롤 내리기
# document.body.scrollHeight = 스크롤하지 않았을 때 전체 높이를 구함.
# 아래 작업을 반복하여 화면높이 변화가 없을 때까지 스크롤 내림.
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

interval = 2
pre_height = browser.execute_script("return document.body.scrollHeight")

# 현재와 이전 높이가 같아질때까지 스크롤을 최하단으로 내림
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if pre_height == curr_height:
        break
    pre_height = curr_height

print("스크롤 완료")

# header = {'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
#                    ,"Accept-Language":"ko-KR,ko"} # 한글 언어 웹페이지를 불러옴
# url = "https://play.google.com/store/games"
# res = requests.get(url, headers=header)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
soup = BeautifulSoup(browser.page_source, "lxml")

# 각 게임 범위 가져옴 (제목, 가격정보, 할인여부, 링크)

# div의 class 가 "kcen6d" 혹은 "kMqehf" 혹은 "kW9Bj" 인것 모두 가져오는 방법
# games = soup.find_all("div", attrs={"class":["kcen6d","kMqehf", "kW9Bj"]})

# 타이틀 정보
games_title = soup.find_all("header", attrs = {"class":"oVnAB"})
print(len(games_title))
for game in games_title:
    # 타이틀정보 출력
    print(game.div.span.get_text())
    
    # 제목, 가격정보, 할인여부, 링크가 포함된 div로 이동
    games_list = game.find_next_sibling("div")
    games_list = games_list.find_all("div", attrs = {"class":"VfPpkd-aGsRMb"})

    # 하위 제목 정보 출력
    for n, game_list in enumerate(games_list,1):
        # 제목 정보 가져오기
        # span element 중에서 sT93pb,DdYX5,OnEJge 세가지 클래스를 가지고 있는 모든 element를 찾음
        title = game_list.select_one("span.sT93pb.DdYX5.OnEJge").get_text()
        price = ""

        # 가격 정보 가져오기 (할인중이지 않은 class와 할인중 class가 다르다.)
        origin_price = game_list.select_one("span.sT93pb.w2kbF.ePXqnb")
        prior_price = game_list.select_one("span.sT93pb.JUF8md.ePXqnb")
        # 원래 가격이 존재한다면
        if origin_price:
            price = origin_price.get_text()
            if price == "" :
                price="무료"
        else :
            price = "가격정보 없음"
        # 할인 시, 할인 가격 + 안내 가져오기
        if prior_price:
            # 할인 전 가격
            price = game_list.select_one("span.sT93pb.w2kbF.Q64Ric").get_text()
            price = prior_price.get_text() +"->"+ price+"(할인중)"
        # 링크
        link = game_list.select_one("a.Si6A0c.Gy4nib")["href"]
        print (str(n)+"번째 게임 : ",title ,"   ", price,"   ", "https://play.google.com"+link)
    
    print("-"*100)

input("종료하려면 enter을 입력하세요")