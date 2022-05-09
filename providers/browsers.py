from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class Chrome:
    """Class defining Chrome webdriver properties"""

    def __init__(self):
        self.options = ChromeOptions()
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("start-maximized")
        self.driver = None

    def init_driver(self):
        """Method for initializing Chrome webdriver"""
        self.driver = webdriver.Chrome(options=self.options)
        return self.driver


class Firefox:
    """Class defining Firefox webdriver properties"""

    def __init__(self):
        self.options = FirefoxOptions()
        self.driver = None

    def init_driver(self):
        """Method for initializing Firefox webdriver"""
        self.driver = webdriver.Firefox(options=self.options)
        return self.driver


class Browsers:
    """Class for mapping browser from the request with browsers classes"""

    @staticmethod
    def get_browser(browser):
        """Method for retrieving browser object according to the request's parameter"""
        _browsers = {"chrome": Chrome(), "firefox": Firefox()}

        return _browsers.get(browser)
