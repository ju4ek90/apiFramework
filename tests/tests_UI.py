import pytest as pytest
# from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from app.ui.cosmos_id_ui import CosmosIDUI


@pytest.fixture(scope="session")
def ui_app():
    driver = webdriver.Chrome(executable_path="/home/yanisimova/Downloads/chromedriver_linux641/chromedriver")
    yield CosmosIDUI(driver)


def test_login_fail(ui_app):
    """Test user can not login with wrong creds"""
    assert ui_app.login("kjhk@kjhk.com", "hkjljk").assert_login_faild() is False
