from TOP_automation.DZ16.PagesDZ16.signup._init_ import SignUp, User
from browser import Browser
import pytest
import time

@pytest.fixture()
def user_test():
    return User(company_email='test@test.com', first_name='FUser', last_name='LUser', company='TestCompany')
@pytest.fixture()
def browser():
    return Browser()
class TestSignUpPage:
    def test_signup(self, browser, user_test):
        browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(10)
        page = SignUp(browser)
        page.SignUp(user_test)
        time.sleep(10)