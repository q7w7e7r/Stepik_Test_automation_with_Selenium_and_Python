import math,time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    link="http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    submit=browser.find_element_by_css_selector('button[type=submit]')
    submit.click()
    # first_window = browser.window_handles[0]
    # new_window= browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    x=browser.find_element_by_id('input_value').text
    answer=browser.find_element_by_id('answer')
    answer.send_keys(f"{calc(x)}")
    submit=browser.find_element_by_css_selector('button[type=submit]')
    submit.click()
finally:
    time.sleep(5)
    browser.close()


