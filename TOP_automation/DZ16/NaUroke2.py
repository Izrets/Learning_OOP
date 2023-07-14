from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

url_login = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

username = browser.find_element(By.NAME, 'username')
username.click()
username.send_keys('Admin')
time.sleep(1)
password = browser.find_element(By.NAME, 'password')
password.click()
password.send_keys('admin123')
time.sleep(1)
btnlogin = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
btnlogin.click()
time.sleep(2)

assert browser.current_url != url_login


browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
time.sleep(1)
browser.find_element(By.CLASS_NAME, 'oxd-userdropdown-link')
time.sleep(1)

assert browser.current_url != url_login