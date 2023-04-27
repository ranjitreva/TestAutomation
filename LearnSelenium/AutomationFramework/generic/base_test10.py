import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from pyjavaproperties import Properties
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


class BaseTest:                              # parent class
    @pytest.fixture(autouse=True)
    def pre_post_condition(self):
        # Create object of Properties class
        property_file = Properties()
        # Open the property file
        property_file.load(open("../config.properties"))
        # Get the value by specifying the key
        browser = property_file['browser']
        url = property_file['url']
        implicit_timeout = property_file['implicit_timeout']
        explicit_timeout = property_file['explicit_timeout']
        usegrid = property_file['usegrid']
        gridurl = property_file['gridurl']

        if usegrid == 'no':
            # Open the browser in local system
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                print("Launched chrome browser in local system")
            else:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
                print("Launched firefox browser in local system")
        else:
            # Open the browser in remote system
            if browser == 'chrome':
                browser_options = Chrome_Options()
                print("Launched chrome browser in remote system")
            else:
                browser_options = Firefox_Options()
                print("Launched firefox browser in remote system")

            # Open the browser in remote system
            self.driver = webdriver.Remote(gridurl, options=browser_options)

        # Maximize the window
        self.driver.maximize_window()
        # Set the timeout [implicit wait]
        self.driver.implicitly_wait(implicit_timeout)
        print("Set implicit timeout : ", implicit_timeout)
        # Set the timeout [explicit wait]
        self.wait = WebDriverWait(self.driver, explicit_timeout)
        print("Set explicit timeout: ", explicit_timeout)
        # Enter the url & wait till the page is completely loaded
        self.driver.get(url)
        print("Enter the url :", url)

        # Close the browser
        yield
        print("Close the browser")
        self.driver.quit()
