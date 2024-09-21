# HTTP METHOD
# get : 어떤 내용을 누구나 볼수 있게 url에 적어서 보내는 방식
# (한번 보낼때 데이터의 양이 제한이있어 큰 데이터를 보낼 수 없음)
# post : url이 아닌 http body에 넣어서 보내는 방식
# (id/pw와 같은 보안이 필요한 업무, 큰 데이터 등을 보낼 수 있음)

import requests
import re
from bs4 import BeautifulSoup

for page in range(1,6):
    url = "https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex="+str(page)
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=header)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    # basicList_item__0T9JD 로 시작하는 class의 모든 element를 가져옴.(정규식 사용)
    items = soup.find_all("div", attrs={"class":re.compile("^basicList_item__0T9JD")})
    # soup.find로 가져온 값에서 다시 find를 통해 하위 element값을 가져올 수 있다.
    items[0].find("div", attrs = {"class":"basicList_info_area__TWvzp"}).div.get_text()
    for item in items:
        
        print("-"*50)
        info = item.find("div", attrs = {"class":"basicList_info_area__TWvzp"})
        # 링크
        href = info.div.a["href"]
        # 제품명
        name = info.find("div", attrs = {"class":"basicList_title__VfX3c"}).get_text()
        if "Apple" in name:
            print("<Apple상품 제외합니다>")
            continue
        # 가격
        price = info.find("div", attrs = {"class":"basicList_price_area__K7DDT"})\
            .strong.span.span.find("span", attrs = {"class":"price_num__S2p_v"}).get_text()
        
        # 광고 제품 제외
        # 광고 태그가 없는 제품을 제외함
        ad_badge = item.find("button", attrs = {"class": "ad_ad_stk__pBe5A"})
        if ad_badge:
            print("<광고 상품 제외합니다>")
            continue
        
        stars = info.find("div", attrs = {"class":"basicList_etc_box__5lkgg"})
    
        # 평점 수
        stars_num = stars.a.em.get_text()
        if not stars_num:
            print("<평점 없는 상품 제외합니다.>")
            continue
            # stars_num = "평점 개수 없음"
        else :
            if int(stars_num.replace(",","")) < 500:
                print("<평점 수 미달 : {}>".format(stars_num))
                continue
        # 평점
        stars = stars.find("span", attrs = {"class":"basicList_star__UzKiv"})
        if not stars:
            print("<별점 없는 상품 제외합니다.>")
            continue
            # stars = "별점 없음"
        else:
            stars = stars.get_text()

        print("제품명 : {}".format(name))
        print("가격 : {}".format(price))
        print("별점 : {}".format(stars))
        print("평점 수 : {}".format(stars_num))
        print("바로가기 : {}".format(href))
