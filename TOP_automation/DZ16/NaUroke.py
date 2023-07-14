from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://guruweba.com/html/teg-table-html-tablitsa-spravochnik-guruweba/')
double_click = browser.find_element(By.XPATH, '/html/body/div[2]/div/main/section/div[1]/div[1]/div/table/tbody/tr[1]/td[1]')
ActionChains(browser).double_click(double_click).perform()

assert double_click.text == 'Ячейка 1'
time.sleep(5)