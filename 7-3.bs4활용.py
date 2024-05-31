# 다음 영화 이미지 2018~2022 년 1~5순위 포스터 가져오기
import requests
from bs4 import BeautifulSoup

for year in range (2018, 2023):
    url = "https://search.daum.net/search?w=tot&q="+str(year)+"%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"thumb_img"})
    for idx,image in enumerate(images):
        image_url = image["src"]
        # image_url 가 `//`로 시작하면 앞에 https: 추가.
        if image_url.startswith("//"):
            image_url = "https:"+image_url
        
        # 이미지 url에 접속 후 페이지의 정보를 파일로 저장하기 위해 새로 접속.
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie{}_{}.png".format(year,idx+1), "wb") as f:
            # image_res가 가지고 있는 content 정보를 바로 파일로 씀
            f.write(image_res.content)
        if idx >=4:
            break