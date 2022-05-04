from selenium.webdriver.common.by import By

from app.ui.base_page import BasePage
from app.ui.urls import Urls


class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//*[@id='email']")
    PASS_FIELD = (By.XPATH, "//*[@id='password']")
    LOGIN_BTN = (By.XPATH, "//*[@id='signInButton']")
    LOGIN_ERR = (By.XPATH, "//div[contains(.,'Password is not correct')]")

    def __init__(self, driver) -> None:
        super(driver)

    def login(self, username, password):
        url = self.prepere_url(Urls.LOGIN)
        self.driver.get(url)

        self.enter_text(username, LoginPage.USERNAME_FIELD)

        self.enter_text(password, LoginPage.PASS_FIELD)

        self.click(LoginPage.LOGIN_BTN)

        return True

    def go_to_register_page(self):
        pass

    def assert_login_faild(self):
        element = self.driver.find_element(LoginPage.LOGIN_ERR)
        if element is not None:
            return True



