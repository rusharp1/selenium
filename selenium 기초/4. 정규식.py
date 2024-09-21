import re

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음.")


# . : 하나의 문자를 의미함.
# (ca.e) : cake, care, case ...
# ^ : 문자열의 시작
# (^de) : desk, demention, dev ...
# $ : 문자열의 끝
# (se$) : case, rase, base ...

# p에 ca.e의 패턴을 입력함.
p = re.compile("ca.e")

# 텍스트의 문자열의 처음부터 p패턴과 일치하면 match객체를 m에 삽입.
# 일치하지 않으면 `None`이 삽입됨
m = p.match("good care")

# 매칭되지 않으면 m.group() 출력 시, 에러가 발생함.
print_match(m)


# 주어진 문자중에 일치하는 것이 있는지 확인
m = p.search("good care")
print_match(m)

m = p.search("careless")
# 일치하는 문자열을 반환함
print("m.group() : ",m.group())
# 입력받은 문자열을 반환함 (string은 함수가 아니라 변수)
print("m.string : ",m.string)
# 입력받은 문자열의 시작 index
print("m.start() : ",m.start())
# 입력받은 문자열의 끝 index
print("m.end() : ",m.end())
# 입력받은 문자열의 시작/끝 index
print("m.span() : ",m.span())

# findall : 패턴과 일치하는 모든 문자열을 리스트 형태로 반환
lst = p.findall("good care case")
print(lst)

# finditer : 패턴과 일치하는 모든 문자열을 match객체로 반환
lst = p.finditer("good care case")
print(lst)


# 문자 클래스 : [ ] 사이의 문자들과 매치
# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자 = /d <-> [^0-9], /D
p = re.compile("[a-z]+")
m = p.search("test")
print(m)

# 반복 : * or + 바로 앞의 문자를 반복함
# ca*t : ct ~ caaaa ... at 까지 매치됨 (a 반복횟수 0회부터)
# ca+t : cat ~ caaa ... at 까지 매치됨 (a 반복횟수 1회부터)
# ca{n,m}t : c(a * n~m회)t 까지 매치됨
# 다만, {}안의 숫자가 한개일 때 정해진 횟수만큼만 반복되어야 함
# ca?t : a 가 있어도 되고 없어도 된다 (=ca{0,1}t)
