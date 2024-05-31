import requests
from bs4 import BeautifulSoup

header = {'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
                   ,"Accept-Language":"ko-KR,ko"} # 한글 언어 웹페이지를 불러옴
url = "https://play.google.com/store/games"
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify()) # html 문서를 보기좋게 출력

# 처음 보이는 5개의 헤더만 가져옴

games_title = soup.find_all("header", attrs = {"class":"oVnAB"})
print(len(games_title))

for game in games_title:
    title = game.find("div", attrs = {"class":"kcen6d"}).get_text()
    print(title)