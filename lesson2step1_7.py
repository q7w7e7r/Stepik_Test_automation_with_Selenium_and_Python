import time,math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element_by_tag_name('img')
    valuex = img.get_attribute('valuex')
    answer = browser.find_element_by_id('answer')
    answer.send_keys(f'{calc(valuex)}')
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id('robotsRule')
    robotsRule.click()
    submit = browser.find_element_by_xpath("//button[text()='Submit']")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()