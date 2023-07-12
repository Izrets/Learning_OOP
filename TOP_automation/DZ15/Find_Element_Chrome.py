from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
link = ('http://example.com')
browser.get(link)
locator = (By.XPATH, "/html/body/div/p[2]/a")
try:
    find = WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))
except:
    browser.quit()
    print('No such element')

if find.text == 'More information...':
    url1 = browser.current_url
    find.click()
    time.sleep(4)
    url2 = browser.current_url
    print('The element found and fits the text')
else:
    print('The text if not found')


if url1 != url2:
    print('The url has been changed')
else:
    print('The url has not been changed')
