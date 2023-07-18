from selenium.webdriver.common.by import By

class Locators:
    email_locator = (By.XPATH, '//*[@id="frontegg-login-box-container-default"]/div[3]/input')
    first_name_locator = (By.XPATH, '//*[@id="frontegg-login-box-container-default"]/div[4]/input')
    last_name_locator = (By.XPATH, '//*[@id="frontegg-login-box-default"]/div[2]/div[1]/div/div/div[2]/form/div[3]/div[2]/input')
    company_name_locator = (By.XPATH, '//*[@id="frontegg-login-box-default"]/div[2]/div[1]/div/div/div[2]/form/div[4]/div[2]/input')
    signup_button_locator = (By.XPATH, '//*[@id="frontegg-login-box-default"]/div[2]/div[1]/div/div/div[2]/form/button')
