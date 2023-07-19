from TOP_automation.DZ16.PagesDZ16.signin._init_ import User, SignIn
from browser import Browser
import pytest
import time

@pytest.fixture()
def user_test():
    return User(email='test@test.com', password='12345678Aa_')
@pytest.fixture()
def browser():
    return Browser()
class TestSSigningInPage:
    def test_signup(self, browser, user_test):
        browser.go_to_site(SignIn.path)
        browser.driver.implicitly_wait(10)
        page = SignIn(browser)
        page.signin(user_test)
        time.sleep(10)
