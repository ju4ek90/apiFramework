from app.ui.page_objects.login_page import LoginPage


class CosmosIDUI:
    """Class defining web app"""

    def __init__(self, driver):
        self.login_page = LoginPage(driver)


