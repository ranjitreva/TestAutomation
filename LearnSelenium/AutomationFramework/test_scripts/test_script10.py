
from generic.base_test10 import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from generic.utility import Excel


class TestInvalidLogin(BaseTest):   # Here we are using inheritance concept (child class)

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)        # Creating an object of login_page
        # Enter invalid username
        login_page.set_username('abcd')
        # Enter invalid password
        login_page.set_password('xyz')
        # Click on login button
        login_page.click_login_button()
        # Verify that the error message is displayed
        result = login_page.verify_error_message_displayed(self.wait)
        assert result
