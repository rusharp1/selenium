<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=BDBDC8&amp;height=150&amp;section=header">

# selenium

> python 과 selenium, bs4 사용하여 웹사이트를 조작 및 응용.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/rusharp1/selenium&count_bg=%233B3B3B&title_bg=%23B178BE&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## 1.dooray 자동화

### 1\. 프로젝트 목록

#### 1. dooray\_contact.py
1. 프로젝트 개요 (Introduction)
    * 이 스크립트는 Selenium과 BeautifulSoup을 사용하여 Dooray Contacts 페이지에서 반복적인 작업을 자동화합니다. 사용자는 새 연락처를 만들거나, 그룹으로 복사하거나, 선택된 연락처를 삭제하는 등의 작업을 쉽게 수행할 수 있습니다. 이 스크립트는 브라우저 자동화 도구인 Selenium과 HTML 파싱을 위한 BeautifulSoup을 결합하여 효율적으로 동작합니다.
2. 기능 설명 (Features) 
    * 새 연락처 생성하기: 사용자 입력을 통해 여러 개의 새 연락처를 생성하고, 각 연락처에 이름, 이메일, 전화번호, URL 등의 정보를 입력합니다.
    * 연락처 그룹 복사: 선택한 연락처를 그룹으로 복사하고, 새로운 그룹을 자동으로 생성하여 연락처를 추가합니다.

4. 명령어 실행 예시 
    <details>
      <summary>명령어 실행 예시 보기/접기</summary>
      
      - 주소록 새 연락처 추가 및 그룹으로 복사 <br>
        https://youtu.be/6JtZ-02TBp0
    
    </details>

 ***

#### 2\. dooray\_mail\.py
1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 Selenium과 BeautifulSoup을 활용하여 Dooray 플랫폼에서 메일 서비스를 자동화하는 Python 스크립트입니다. 사용자는 원하는 작업을 선택하여 웹메일을 탐색하고, 메일을 전송하며, 메일 목록과 상세보기의 타이틀바 버튼을 가져올 수 있습니다.
2. 기능 설명 (Features) 
    * 메일 전송 : 수신자의 이메일을 입력하고, 제목가 본문을 작성하여 메일을 전송합니다. 전송 성공 여부에 대한 확인도 제공합니다.
    * 메일 목록 타이틀바 가져오기 :  받은 메일함 및 기타 메일 폴더에서 타이틀바에 있는 버튼 목록을 추출합니다. 버튼 정보는 title_bar_list 딕셔너리로 저장됩니다.
    * 메일 상세보기 타이틀바 버튼 가져오기 : 메일 상세보기를 통해 해당 메일의 타이틀바에 있는 버튼 목록을 추출합니다. 다양한 뷰 타입 (분할 뷰, 목록 뷰, 시간순 뷰 등) 에 따른 결과를 제공합니다.

4. 명령어 실행 예시 
    <details>
      <summary>명령어 실행 예시 보기/접기</summary>
      
      - 메일 새 메일 쓰기<br>
        https://youtu.be/lJjq90E0KYI
        
      - 메일 목록 화면 타이틀바 목록 확인하기<br>
        https://youtu.be/DitRqsag10o
        
      - 메일 상세보기 화면 타이틀바 목록 확인하기<br>
        https://youtu.be/xM-4I1Ju61I
    </details>

***
#### 3\. dooray\_project\.py

1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 Selenium과 BeautifulSoup을 활용하여 Dooray 플랫폼에서 프로젝트 관리 작업을 자동화하는 Python 스크립트입니다. 사용자는 원하는 작업을 선택하여 프로젝트에 업무, 태그, 마일스톤 등을 손쉽게 추가할 수 있습니다.
2. 기능 설명 (Features)
    * 업무 생성: 사용자가 지정한 개수만큼의 업무를 프로젝트에 추가합니다.
    * 메일 생성: 프로젝트에 10개의 메일 주소를 자동으로 생성합니다.
    * 태그 추가: 사용자가 설정한 다양한 태그를 프로젝트에 추가합니다.
    * 마일스톤 추가: 기간이 있는 마일스톤과 없는 마일스톤을 각각 추가합니다.
    * 댓글 작성: 특정 업무에 대해 20개의 댓글을 자동으로 작성합니다.
    * UI 자동화: Selenium을 통해 웹 브라우저를 자동으로 제어하여 사용자 작업을 시뮬레이션합니다.
3. 명령어 실행 예시
    <details>
      <summary>명령어 실행 예시 보기/접기</summary>
      
      - 프로젝트 업무 추가  
        https://youtu.be/5_KhX62uhp4
        
      - 프로젝트 메일 주소 추가  
        https://youtu.be/HjCuZdZteQk
        
      - 프로젝트 태그 추가  
        https://youtu.be/w36x14DlA00
        
      - 프로젝트 마일스톤 추가  
        https://youtu.be/3Cfc3W3_BGc
    
    </details>
***
### 2\. 사전 요구사항 \(Prerequisites\)

* Python 3.x 설치
* `selenium` 라이브러리 설치
* `beautifulsoup4` 라이브러리 설치
* `lxml` 라이브러리 설치
* `webdriver_manager` 라이브러리 설치
***
### 3\. 참고사항 \(Notes\)

* dooray는 상품 별 환경 조합이 약 10가지 이상이고, 해당 환경에서 테스트웨어 생성을 위해 생성한 스크립트입니다.
* 해당프로젝트는 2023년 09월 기준으로 작성된 프로젝트입니다.
웹사이트 업데이트로 인해 버튼이나 요소 변경으로 인해 실행이 되지 않을 수 있습니다.
* 해당 프로젝트는 dooray 도메인과 id/pw 를 필요로 합니다. 로그인 보안에 유의해주세요.
***
### 4\. 설치 및 실행 방법 \(Installation\)

1. 필요한 라이브러리를 설치합니다.

    ```
    pip install selenium beautifulsoup4 lxml
    ```
2. 프로젝트를 로컬에 클론합니다.
    ```
    git clone -b master https://github.com/rusharp1/selenium.git
    ```
4. ChromeDriver를 설치하고, 시스템 PATH에 추가합니다. Chrome 버전과 맞는 드라이버를 다운로드해야 합니다.
5. 전역변수 domain 에 본인의 domain  을 입력합니다.
6. 전역변수 id, pw 에 본인의 id와 비밀번호를 입력합니다.
7. 해당 프로젝트 위치로 이동합니다.
    ```
    cd ./selenium/"dooray 자동화"
    ```
8. 원하는 프로젝트를 실행합니다.

    ```
    파일명.py
    ```


## 2. 네이버 숙소예약 자동화
### 1\. 프로젝트 목록


## 3.selenium 기초 (Selenium Basics)
### 1. 개요 (Overview)

#### 1. 저장소 개요  (Repository Overview)
*  이 저장소는  [Inflearn](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9-%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91#curriculum)의 Selenium 기초 강의를 기반으로 한 연습 문제와 예제를 담고 있습니다.
* 더 자세한 내용을 보고싶다면, [blog](https://rusharp.tistory.com/category/python/python_selenium) 에서 확인 가능합니다.

#### 2. 강의 개요 (Course Overview) 
* 이 강의는 Selenium 을 사용하여 파이썬으로 웹 브라우저를 자동화하고, 웹 스크래핑 및 크롤링 작업을 실습하는 데 중점을 둡니다.
다양한 도구와 라이브러리를 학습하며, 기본부터 고급 주제까지 다룹니다.
*** 
### 2. 주요 학습 내용 (Main Learning Contents)

#### 1. 웹 스크래핑 소개 (Introduction to Web Scraping)
1. 웹 스크래핑이란?
    - 웹 스크래핑은 웹사이트로부터 데이터를 자동으로 추출하는 과정을 말합니다. 이는 API가 제공되지 않는 웹사이트에서 데이터를 수집할 때 유용합니다.

#### 2. HTML 및 CSS 이해  (Understanding HTML and CSS)
   - HTML 구조: 요소, 태그, 속성에 대한 이해
   - CSS 선택자: 스타일을 기반으로 요소를 찾고 추출하는 방법
   - 웹 스크래핑 준비: 페이지에서 적절한 요소를 대상으로 하는 패턴 식별


 ***
### 3. 도구 및 라이브러리 (Tools and Libraries)
   - **BeautifulSoup**: HTML과 XML 문서를 파싱하는 파이썬 라이브러리로, 파싱된 트리를 쉽게 검색하고 수정할 수 있습니다.
   - **Requests**: 웹 페이지에 요청을 보내는 데 사용되는 간단하고 우아한 HTTP 라이브러리.
   - **Selenium**: 파이썬을 통해 웹 브라우저와 상호작용할 수 있도록 하는 도구로, 동적 콘텐츠 스크래핑에 유용합니다.
   - **lxml** : XPath 사용을 가능하게 하는 빠르고 성능이 뛰어난 XML 및 HTML 처리 라이브러리.



 ***
### 4\. 설치 및 실행 방법 \(Installation\)
1. 필요한 라이브러리를 설치합니다.
 
    ```
    pip install selenium beautifulsoup4 lxml
    ```
2. 프로젝트를 로컬에 클론합니다.
    ```
    git clone -b master https://github.com/rusharp1/selenium.git
    ```
3. ChromeDriver를 설치하고, 시스템 PATH에 추가합니다. Chrome 버전과 맞는 드라이버를 다운로드해야 합니다.
4. 해당 프로젝트 위치로 이동합니다.
    ```
    cd ./selenium/"selenium 기초"
    ```
5. 원하는 프로젝트를 실행합니다.

    ```
    파일명.py
    ```

## 4\. LICENSE

이 프로젝트는 [MIT License](LICENSE) 에 따라 라이선스가 부여됩니다.

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=BDBDC8&amp;height=150&amp;section=footer">


