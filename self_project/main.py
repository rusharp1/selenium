from test_hotelnaver import hotel_naver_search
from selenium import webdriver

def main():
    # chrome driver 를 사용하여 네이버 호텔 예약 페이지 이동
    url = "https://hotels.naver.com/"
    browser = webdriver.Chrome()
    browser.get(url)
    hotel_naver_search(browser)

if __name__== "__main__":
   main()
   