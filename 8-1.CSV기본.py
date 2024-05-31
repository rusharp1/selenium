import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액1-200.csv"
# excel에서 열 때 한글이 깨지면 encoding을 `utf-8-sig`로 작성.
# 파일을 쓰기모드로 오픈 후 파일객체를 csv.writer 에 넣음.
f =open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# string.split("구분자") = 구분자를 기준으로 string을 나눈 뒤 리스트로 삽입
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# writer.writerow를 통해 list data를 한 라인씩 추가함.
writer.writerow(title)

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rouws = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rouws:
        columns = row.find_all("td")
        # 중간에 여백 등을 위해 비어있는 td는 스킵함.
        if len(columns)<2:
            continue

        # tc중에 값이 있는 내용을 가져온 뒤 여백 삭제
        data = [column.get_text().strip() for column in columns]
        print(data)
        writer.writerow(data)
# f.close()를 사용해서 닫아주는것이 좋음.
f.close()