
from generic.base_test10 import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from generic.utility import Excel


class TestInvalidLogin(BaseTest):   # Here we are using inheritance concept (child class)

    def test_invalid_login(self):
        user_name = Excel.get_cell_value("../data/Input.xlsx", "invalid_login", 2, 1)   # Creating an object of user_name [get_cell_value(file_path, sheet, row, col)]
        password = Excel.get_cell_value("../data/Input.xlsx", "invalid_login", 2, 2)    # Creating an object of password [get_cell_value(file_path, sheet, row, col)]
        login_page = LoginPage(self.driver)        # Creating an object of login_page
        # Enter invalid username
        login_page.set_username(user_name)
        # Enter invalid password
        login_page.set_password(password)
        # Click on login button
        login_page.click_login_button()
        # Verify that the error message is displayed
        result = login_page.verify_error_message_displayed(self.wait)
        assert result
