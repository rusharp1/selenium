import requests
url = "https://www.melon.com"
# uster_agent를 입력함으로서 실제 크롬에서 접속하는것과 동일한 결과를 받을 수 있음.
header = {'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")}
# 응답코드가 403이면 권한없음.
res = requests.get(url, headers=header)
# res.raise_for_status()
print("응답코드 : ",res.status_code)
# mygoogle.html 을 쓰기모드로 열고 res.text를 입력.
with open("melon.html", "w", encoding="utf8") as f:
    f.write(res.text)