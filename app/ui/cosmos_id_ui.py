from app.ui.base_page import BasePage
from app.ui.page_objects.login_page import LoginPage


class CosmosIDUI(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.login_page = LoginPage()

    def login(self):
        self.login_page.login()
