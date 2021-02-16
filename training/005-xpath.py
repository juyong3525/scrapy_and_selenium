from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument(
    "User-Agent:  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36")
options.add_argument("lang=ko_KR")

chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver, options=options)
driver.get('https://entertain.v.daum.net/v/20190711174023188')

title = driver.find_element_by_xpath("//h3[@class='tit_view']")
print(title.text)
driver.quit()
