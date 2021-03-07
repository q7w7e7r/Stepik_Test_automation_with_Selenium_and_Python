import math,time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x=browser.find_element_by_id("input_value")
    x_value=x.text
    answer =  browser.find_element_by_id("answer")
    answer.send_keys(f"{calc(x_value)}")
    check_box=browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    check_box.click()
    radio_btn = browser.find_element_by_xpath("//label[@for='robotsRule']")
    radio_btn.click()
    submit = browser.find_element_by_xpath("//button[text()='Submit']")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()