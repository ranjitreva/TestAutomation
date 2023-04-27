import pytest

from generic.base_test10 import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from generic.utility import Excel


class TestValidLogin(BaseTest):   # Here we are using inheritance concept (child class)
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        user_name = Excel.get_cell_value("../data/Input.xlsx", "valid_login", 2, 1)   # Creating an object of user_name [get_cell_value(file_path, sheet, row, col)]
        password = Excel.get_cell_value("../data/Input.xlsx", "valid_login", 2, 2)    # Creating an object of password [get_cell_value(file_path, sheet, row, col)]
        login_page = LoginPage(self.driver)        # Creating an object of login_page
        # Enter valid username
        login_page.set_username(user_name)         # Call the method
        # Enter valid password
        login_page.set_password(password)          # Call the method
        # Click on login button
        login_page.click_login_button()
        # Verify that the home page is displayed.
        home_page = HomePage(self.driver)            # Creating an object of home_page
        result = home_page.verify_home_page_is_displayed(self.wait)
        assert result
