from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument(
    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(chromedriver, options=options)

driver.get('https://news.v.daum.net/v/20210211144601206')
title = driver.find_element_by_css_selector('head > title')
print(title.get_attribute('text'))
