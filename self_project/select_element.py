# 특정 element를 찾는 동안 최대 5초동안 기다린 뒤, 반환하는 class입니다.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

def select_element(browser, element, name):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located\
                                         ((element, name)))
        return browser.find_element(element, name)
    except TimeoutException:
        pytest.fail(f"타임아웃: 해당 element를 찾을 수 없습니다: {str(element)} {name}")

def select_elements(browser,element, name):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located\
                                         ((element, name)))
        return browser.find_elements(element, name)
    except TimeoutException:
        pytest.fail(f"타임아웃: 해당 element를 찾을 수 없습니다: {str(element)} {name}")