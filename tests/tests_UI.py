import pytest as pytest
from selenium import webdriver
from app.ui.cosmos_id_ui import CosmosIDUI


@pytest.fixture(scope="session")
def ui_app():
    """Fixture for initializing web app instance CosmosIDUI()"""
    driver = webdriver.Chrome()
    yield CosmosIDUI(driver)
    driver.quit()


def test_login_fail(ui_app):
    """Test user can not login with wrong creds"""
    ui_app.login_page.login("kjhk@kjhk.com", "hkjljk")
    ui_app.login_page.assert_login_faild()
