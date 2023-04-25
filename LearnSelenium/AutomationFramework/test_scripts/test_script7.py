import time

from generic.base_test7 import BaseTest
from pages.login_page import LoginPage


class TestValidLogin(BaseTest):    # Here we are using inheritance concept (child class)

    def test_valid_login(self):
        login_page = LoginPage(self.driver)  # Creating an object of it
        # Enter valid username
        login_page.set_username("admin")
        # Enter valid password
        login_page.set_password("manager")
        # Click on login button
        login_page.click_login_button()
        # Verify that the home page is displayed.
        time.sleep(5)