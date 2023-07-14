from selenium import webdriver
from selenium.webdriver import Keys
from TOP_automation.DZ16.PagesDZ16.signup.locators import Locators

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element(self.locator[0], self.locator[1])

    def click_element(self):
        self.element_click()

class InputElement(Element):
    def enter_txt(self, text):
        self.click_element()
        self.element.send_keys(text)

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)

    def get_text(self):
        return self.element.get_attribute('value')
class ButtonElement(Element):
    def key_code(self):
        return self.element.send_keys(Keys.ENTER)