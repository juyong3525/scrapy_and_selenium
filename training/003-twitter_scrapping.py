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

driver.get('https://twitter.com/login')
id_field = driver.find_element_by_name("session[username_or_email]")
id_field.clear()
id_field.send_keys('ID')  # git에 push X
pw_field = driver.find_element_by_name("session[password]")
pw_field.clear()
pw_field.send_keys('PWD')   # git에 push X
pw_field.send_keys(Keys.RETURN)

time.sleep(2)

data = driver.find_elements_by_css_selector(
    'div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1mi0q7o > div:nth-child(2) > div:nth-child(1) > div > span:nth-child(1)')
for item in data:
    print(item.text)

driver.quit()
