import urllib

from config.config import Config


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def prepere_url(self, url):
        return urllib.parse.urljoin(Config.BASE_URL, url)

    def enter_text(self, text, element):
        element = self.driver.find_element(**element)
        element.send_keys(text)

    def click(self, element):
            element = self.driver.find_element(**element)
            element.click()


