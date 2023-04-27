from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Class code is separate
class LoginPage:
    # [Declaration] Private variable
    __username = (By.ID, "username")
    __password = (By. NAME, "pwd")
    __login_button = (By.XPATH, "//div[. = 'Login ']")
    __error_message = (By.XPATH, "//span[contains(text(), 'invalid')]")

    # [Initialization]
    def __init__(self, driver):
        self.__driver = driver

    # [Utilization] To access it, the only way is to use a method. self is an instance variable. self belongs to an object.
    def set_username(self, username):
        self.__driver.find_element(*self.__username).send_keys(username)

    def set_password(self, password):
        self.__driver.find_element(*self.__password).send_keys(password)

    def click_login_button(self):
        self.__driver.find_element(*self.__login_button).click()

    def verify_error_message_displayed(self, wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__error_message))
            print("Error message is displayed")
            return True
        except:
            print("Error message is not displayed")
            return False
