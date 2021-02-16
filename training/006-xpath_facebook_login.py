from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/chromedriver')
driver.get('https://www.facebook.com/')

user_name = '######'    # git push X
password = '######'    # git push X
email_id = "//*[@id='email']"
password_id = "//*[@id='pass']"
login_btn = "//div[@class='_6ltg']/button"


email_tag = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, email_id)
    )
)
password_tag = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, password_id)
    )
)
login_btn_tag = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, login_btn)
    )
)

email_tag.clear()
email_tag.send_keys(user_name)
password_tag.clear()
password_tag.send_keys(password)
login_btn_tag.click()

time.sleep(3)

driver.quit()
