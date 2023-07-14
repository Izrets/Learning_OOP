from selenium import webdriver
from selenium.webdriver.common.by import By
from TOP_automation.DZ16.PagesDZ16.signup.element import Element, InputElement, ButtonElement
from TOP_automation.DZ16.PagesDZ16.signup.locators import Locators

class User:
    def __init__(self, company_email, first_name, last_name, company):
        self.company = company
        self.last_name = last_name
        self.first_name = first_name
        self.company_email = company_email
        
class SignUp:
    path = '/account/sign-up'
    def __init__(self, browser):
        self.company_email = InputElement(driver=browser.get_driver(), locator=Locators.company_email_locator)
        self.first_name = InputElement(driver=browser.get_driver(), locator=Locators.first_name_locator)
        self.last_name = InputElement(driver=browser.get_driver(), locator=Locators.last_name_locator)
        self.company = InputElement(driver=browser.get_driver(), locator=Locators.company_name_locator)
        self.signup_button = ButtonElement(driver=browser.get_driver(), locator=Locators.signup_button_locator)
    def signup(self, user: User):
        self.company_email.enter_txt(user.company_email)
        self.first_name.enter_txt(user.first_name)
        self.last_name.enter_txt(user.last_name)
        self.company.enter_txt(user.company)
        self.signup_button.key_code()
        