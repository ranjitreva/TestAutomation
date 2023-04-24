import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pyjavaproperties import Properties


class BaseTest:                                # parent class
    @pytest.fixture(autouse=True)
    def pre_post_condition(self):
        # Create object of Properties class
        property_file = Properties()
        # Open the property file
        property_file.load(open("../config.properties"))
        # Get the value by specifying the key
        browser = property_file['browser']
        url = property_file['url']
        timeout = property_file['timeout']

        # Open the google chrome browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Maximize the window
        self.driver.maximize_window()
        # Set the timeout
        self.driver.implicitly_wait(timeout)
        # Enter the url & wait till the page is completely loaded
        self.driver.get(url)
        # Close the browser
        yield
        self.driver.close()
