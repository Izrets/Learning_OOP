# Продолжить работу с Selenium. Проверить строку поиска python.org.
# Сделать какой-нибудь запрос на странице python.org в pycharm.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link = "https://www.python.org/"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(link)
    field_input = browser.find_element(By.ID, "id-search-field")
    field_input.click()
    field_input.send_keys("testing")
    browser.find_element(By.CLASS_NAME, "search-button").click()

finally:

    time.sleep(2)
    browser.quit()