from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Class code is separate
class HomePage:
    # [Declaration] Private variable
    __logout = (By.ID, "logoutLink")

    # [Initialization]
    def __init__(self, driver):
        self.__driver = driver

    # [Utilization] To access it, the only way is to use a method. self is an instance variable. self belongs to an object.
    def verify_home_page_is_displayed(self, wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__logout))
            print("Home page is displayed")
            return True
        except:
            print("Home page is not displayed")
            return False
