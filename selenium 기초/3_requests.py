import requests

# 응답코드가 403이면 권한없음.
res = requests.get("https://rusharp.tistory.com/18")
print("응답코드 : ",res.status_code) #403

# 응답코드가 200이면 정상
res = requests.get("http://nadocoding.tistory.com")
print("응답코드 : ",res.status_code)

res = requests.get("https://google.com")
print("응답코드 : ",res.status_code)

# requests.codes.ok == 200
if res.status_code == requests.codes.ok:
    print("정상입니다.")
else :
    print("문제가 생겼습니다. [에러코드 : {}]".format(res.status_code))

# html 을 올바로 가져오는 경우 pass
# html 을 가져오는 중 오류발생 시, 에러발생 진행.
res.raise_for_status()
print("웹 스크래핑을 진행합니다.")

# res 의 html 값을 가져옴.
# print(res.text)

# mygoogle.html 을 쓰기모드로 열고 res.text를 입력.
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)