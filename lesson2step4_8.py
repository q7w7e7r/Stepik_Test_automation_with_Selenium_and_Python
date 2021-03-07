from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math,time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    lilk="http://suninjuly.github.io/explicit_wait2.html"
    browser=webdriver.Chrome()
    browser.get(lilk)
    price=WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'100')
    )
    button_book=browser.find_element_by_id('book')
    button_book.click()
    x=browser.find_element_by_id('input_value').text
    answer=browser.find_element_by_id('answer')
    answer.send_keys(f'{calc(x)}')
    submit=browser.find_element_by_id('solve')
    submit.click()
finally:
    time.sleep(3)
    browser.close()
