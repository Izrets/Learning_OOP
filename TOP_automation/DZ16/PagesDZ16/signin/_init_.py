from selenium import webdriver
from selenium.webdriver.common.by import By
from TOP_automation.DZ16.PagesDZ16.signin.element import Element, InputElement, ButtonElement
from TOP_automation.DZ16.PagesDZ16.signin.locators import Locators


class SigningIn:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class SignIn:
    path = '/account/login'

    def __init__(self, browser):
        self.email = InputElement(driver=browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=Locators.password_locator)
        self.signin_button = ButtonElement(driver=browser.get_driver(), locator=Locators.signin_button_locator)

    def signin(self, user: SigningIn):
        self.email.enter_txt(SigningIn.email)
        self.password.enter_txt(SigningIn.password)
        self.signin_button.key_code()
