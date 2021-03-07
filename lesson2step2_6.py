import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x=browser.find_element_by_id('input_value').text
result=calc(x)
answer=browser.find_element_by_id('answer')
answer.send_keys(f'{result}')
robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()
robotsRule = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()