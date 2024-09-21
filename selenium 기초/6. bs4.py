# BeautifulSoup : 스크래핑을 하기위해 사용하는 패키지이고
# lxml : xml을 해석하는 파서

import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
res = requests.get(url)
res.raise_for_status()

# res.text 를 lxml파서를 통해 beautifulsoup 객체로 만듬.
soup = BeautifulSoup(res.text, "lxml")

# html 에서 첫번째로 발견되는 title 값을 가져옴.
print(soup.title)
# title값의 text값만 가져옴.
print(soup.title.get_text())

print(soup.link)
# link태그가 가지고있는 속성을 가져옴.
print(soup.link.attrs)

# link 태그 안의 특정 속성을 출력
print(soup.link['rel'])
print(soup.link.attrs['rel'])


# soup 객체중 a태그, class속성이 일치하는 첫번째 엘리먼트 가져옴.
test = soup.find("a", attrs = {"class" : "_NM_THEME_CATE tab id_bboom"})
# 속성값만 할당함
test = soup.find(attrs = {"class" : "_NM_THEME_CATE tab id_bboom"})
print(test)

list1 = soup.find("li", attrs = {"class" : "nav_item"})
print(list1)
# list1에 들어있는 값 중 i 값만 출력
print(list1.i)


## 다음값으로 이동

print(list1.a.get_text())

# list1엘리먼트로부터 다음 엘리먼트(형재 관계) 로 넘어감.
# 태그 사이의 개행정보가 있어서 next_sibling을 2회해야할 수도 있음.
print(list1.next_sibling.next_sibling)

list2 = list1.next_sibling.next_sibling
list3 = list2.next_sibling.next_sibling

print(list3.get_text())

# 다음 sibling으로 가는데 "li"와 일치하는 태그를 찾음.
list2 = list1.find_next_sibling("li")
print(list2.get_text())

# list2 기준으로 다음 형제들을 모두 가져옴.

print("="*25 + "list2.find_next_siblings(\"li\")"+"="*25)
print(list2.find_next_siblings("li"))


## 이전값으로 이동 
list2 = list3.previous_sibling.previous_sibling
print(list2.get_text())


## 부모 태그로 이동.
# list1의 부모 태그로 이동함.
print(list1.parent)
print("-"*40)

test = soup.find("a", text = "로그인")
print(test)