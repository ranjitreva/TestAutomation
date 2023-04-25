from selenium.webdriver.common.by import By


# Class code is separate
class LoginPage:
    # [Declaration] Private variable
    __username = (By.ID, "username")
    __password = (By. NAME, "pwd")
    __login_button = (By.XPATH, "//div[. = 'Login ']")

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
