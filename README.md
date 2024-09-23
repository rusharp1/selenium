selenium 의 기본적인 내용을 공부하고 현업에서 실습해본 내용입니다.


제가 진행한 협업 도구 환경에서는 상품 별 환경 조합이 약 10가지 이상 되었습니다.
이 모든 환경에 대한 테스트웨어 생성에 한계를 느끼는 동시에, CI/CD 프로세스에서의 테스트 환경 자동화의 중요성을 인지하였습니다.
python 자동화 폴더에 python, selenium 및 bs4 를 사용한 `테스트 환경 생성` 중 일부를 정리했습니다.

아래는 python 자동화 폴더 내에 포함되어있는 코드를 직접 실행한 영상입니다.



    
- 주소록 새 연락처 추가 및 그룹으로 복사
    
    https://youtu.be/6JtZ-02TBp0
    
- 메일 새 메일 쓰기
    
    https://youtu.be/lJjq90E0KYI
    
- 메일 목록 화면 타이틀바 목록 확인하기
    
    https://youtu.be/DitRqsag10o
    
- 메일 상세보기 화면 타이틀바 목록 확인하기
    
    https://youtu.be/xM-4I1Ju61I


  #### 3. dooray\_project.py
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
