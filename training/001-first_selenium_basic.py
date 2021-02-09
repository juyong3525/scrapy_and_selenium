from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromedriver 사용
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'
# driver = webdriver.Chrome(chromedriver)

# phantomJS 사용
# phantomjs_file = '/usr/local/bin/phantomjs'
# driver = webdriver.PhantomJS(phantomjs_file)

# headless chrome 사용
chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'
headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
headless_options.add_argument('window-size=1920x1080')
headless_options.add_argument('disable-gpu')
headless_options.add_argument(
    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
headless_options.add_argument('lang=ko_KR')

driver = webdriver.Chrome(chromedriver, options=headless_options)


driver.get('http://www.python.org')
print(driver.title)
print(driver.current_url)
print()

assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys("python")
elem.send_keys(Keys.RETURN)
time.sleep(2)

assert "No results found." not in driver.page_source

data = driver.find_elements_by_css_selector(
    "#content > div > section > form > ul > li > h3 > a")
for item in data:
    print(item.text)

driver.quit()
