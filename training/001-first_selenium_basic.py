from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.python.org')
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys("python")
elem.send_keys(Keys.RETURN)
time.sleep(2)

assert "No results found." not in driver.page_source

h3s = driver.find_elements_by_tag_name('h3')
for h3 in h3s:
    print(h3.text)

driver.quit()
