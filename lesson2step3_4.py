import math,time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/alert_accept.html"
  browser.get(link)
  button = browser.find_element_by_css_selector('button[type=submit]')
  button.click()
  alert = browser.switch_to.alert
  alert.accept()
  x = browser.find_element_by_id('input_value').text
  answer=browser.find_element_by_id('answer')
  answer.send_keys(f"{calc(x)}")
  submit=browser.find_element_by_css_selector('button[type=submit]')
  submit.click()
finally:
  time.sleep(5)
  browser.close()