import os
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

name=browser.find_element_by_css_selector('input[name=firstname]')
name.send_keys('Alex')
lastname=browser.find_element_by_css_selector('input[name=lastname]')
lastname.send_keys('Dem')
email=browser.find_element_by_css_selector('input[name=email]')
email.send_keys('AlDem@test.ru')
file=browser.find_element_by_css_selector('input[type=file]')
cur_dir=os.path.dirname(__file__)
name_file='empty.txt'
file.send_keys(os.path.join(cur_dir,name_file))
submit = browser.find_element_by_css_selector('button[type=submit]')
submit.click()

