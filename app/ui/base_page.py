import urllib
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from config.config import Config


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def prepere_url(self, url):
        return urllib.parse.urljoin(Config.BASE_URL, url)

    def enter_text(self, text, element):
        """Reimplementation of find and enter text into text element"""
        element = self.driver.find_element(*element)
        element.send_keys(text)

    def click(self, element):
        """Reimplementation of find element and click on it"""
        element = self.driver.find_element(*element)
        element.click()

    def get_element(self, element):
        """Reimplementation of find element"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        return element

    def is_element_present(self, element, timeout=3):
        """Method-waiter, checking that element is present on the page"""
        try:
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(element)
            )
        except TimeoutException:
            return False
        return True
