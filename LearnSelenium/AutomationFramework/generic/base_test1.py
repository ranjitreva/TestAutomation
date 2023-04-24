import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class BaseTest:                                # parent class
    @pytest.fixture(autouse=True)
    def pre_post_condition(self):
        # Open the google chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Maximize the window
        driver.maximize_window()
        # Wait up to 10 seconds [Set the timeout]
        driver.implicitly_wait(10)
        # Enter the url & wait till the page is completely loaded
        driver.get('https://aksharatraining.com/')
        # Close the browser
        yield
        driver.close()
