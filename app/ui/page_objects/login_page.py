from selenium.webdriver.common.by import By

from app.ui.base_page import BasePage
from app.ui.urls import Urls


class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//*[@id='email']")
    PASS_FIELD = (By.XPATH, "//*[@id='password']")
    LOGIN_BTN = (By.XPATH, "//*[@id='signInButton']")
    LOGIN_ERR = (By.XPATH, "//div[contains(.,'Password is not correct')]")
    FIRST_MESSAGE = (By.XPATH, "//button[contains(.,'Do not show again')]")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        url = self.prepere_url(Urls.LOGIN)
        self.driver.get(url)
        self.click(element=self.FIRST_MESSAGE)

        self.enter_text(text=username, element=self.USERNAME_FIELD)
        self.enter_text(text=password, element=self.PASS_FIELD)
        self.click(element=self.LOGIN_BTN)

    def go_to_register_page(self):
        pass

    def assert_login_faild(self):
        self.is_element_present(self.LOGIN_ERR)

