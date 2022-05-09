import pytest as pytest

from app.ui.cosmos_id_ui import CosmosIDUI


@pytest.fixture(scope="session")
def ui_app(request):
    """Fixture for initializing web app instance CosmosIDUI()"""
    browser = request.config.getoption("browser")
    app = CosmosIDUI(browser)
    app.launch_browser()
    yield app
    app.quit()


def test_login_fail(ui_app):
    """Test user can not login with wrong creds"""
    ui_app.login_page.login("kjhk@kjhk.com", "hkjljk")
    assert ui_app.login_page.assert_login_faild() is True
