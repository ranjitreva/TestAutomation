
from generic.base_test8 import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestValidLogin(BaseTest):   # Here we are using inheritance concept (child class)

    def test_valid_login(self):
        login_page = LoginPage(self.driver)               # Creating an object of login_page
        # Enter valid username
        login_page.set_username("admin")
        # Enter valid password
        login_page.set_password("manager")
        # Click on login button
        login_page.click_login_button()
        # Verify that the home page is displayed.
        home_page = HomePage(self.driver)                    # Creating an object of home_page
        result = home_page.verify_home_page_is_displayed(self.wait)
        assert result
