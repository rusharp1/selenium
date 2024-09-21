# 웹스크래핑을 이용하여 나만의 비서를 만들기
# 1. 네이버에서 오늘 서울의 날씨 정보를 가져옴.
# 2. 다음 뉴스 홈에서 뉴스 3건을 가져옴 (헤드라인이 현재 사라짐)
# 3. it뉴스 3건을 가져온다.
# 4. 해커스 어학원 홈페이지에서 오늘의 회화 지문을 가져온다.

from bs4 import BeautifulSoup
import requests
import random
import re


def create_soup(url):
    print("="*50)
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=header)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def naver_weather():
    # 1. 네이버에서 오늘 서울의 날씨 정보를 가져옴.
    url = "https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    temp_up = soup.select_one("span.temperature.up").get_text()
    weather = soup.select_one("span.weather.before_slash").get_text()
    temp_today = soup.select_one("span.temperature_inner").select("span")
    low_temp_today = temp_today[0].get_text()
    hight_temp_today = temp_today[2].get_text()
    temp_now = soup.select_one("div.temperature_text").get_text()

    rain_today = soup.find("div", attrs = {"class":"cell_weather"})\
        .find_all("span", attrs={"class":"rainfall"})
    hazy = soup.select(".item_today.level1")
    print
    print("[오늘의 날씨]")
    print(f"{weather}, 어제보다 {temp_up}")
    print(f"현재 {temp_now}(최저 {low_temp_today} / 최고 {hight_temp_today})")
    print(f"오전 강수 확률 {rain_today[0].get_text()} / 오후 강수 확률 {rain_today[1].get_text()}\n")
    print(f"{hazy[0].find('a').get_text().strip()}")
    print(f"{hazy[1].find('a').get_text().strip()}")

def daum_headline_news():
    # 2. 다음 뉴스 홈에서 뉴스 3건을 가져옴
    url = "https://news.daum.net/"
    soup = create_soup(url)

    # 뉴스 리스트를 받아옴
    news_list = soup.find("ul", attrs={"class":"list_newsissue"})
    # find_all(element, limit = n) : n개까지 찾음.
    news_title_list = news_list.find_all("strong", attrs={"class":"tit_g"},limit=10)
    # 랜덤 3개의 뉴스를 가져옴.
    nums = random.sample(range(1, len(news_title_list)),3)
    print("[헤드라인 뉴스]")
    for n, num in enumerate(nums):
        print(f"{n+1}. {news_title_list[num].get_text().strip()}")
        print(f"(링크 : {news_title_list[num].a['href']})")

def naver_it_news():
    # 3. it뉴스 3건을 가져온다.
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)

    # 뉴스 리스트를 받아옴
    news_list = soup.find_all("div", attrs={"class":"cluster_text"})
    print("[IT 뉴스]")
    # 그중 최상위 3개의 뉴스 제목 및 링크를 가져옴
    for n in range(0,3):
        print(f"{n+1}. {news_list[n].find('a').get_text().strip()}")
        print(f"(링크 : {news_list[n].a['href']})")

def hackers():
    # 4. 해커스 어학원 홈페이지에서 오늘의 회화 지문을 가져온다.
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)

    text_lines = soup.find_all("div", attrs={"id": re.compile("^conv_kor")})
    print("[오늘의 영어 회화]")
    print("(영어 지문)")
    # text_lines를 슬라이싱하여 절반이후부터 끝까지 출력
    for text_line in text_lines[len(text_lines)//2:]:
        print(text_line.get_text().replace("\n", ""))
    print("(한글 지문)")
    for text_line in text_lines[:len(text_lines)//2]:
        print(text_line.get_text().replace("\n", ""))
    
# 코드를 직접 실행했을 때, 동작함.
if __name__ == "__main__":
    naver_weather()
    daum_headline_news()
    naver_it_news()
    hackers()