import pytest as pytest

from app.api.api_client import ApiClient


@pytest.fixture(scope="session")
def get_token():
    ac = ApiClient()
    ac.login()
    yield ac


def test_root_folder_succesfull(get_token):
    assert get_token.get_root_folder() is not None


def test_specific_folder_succesfull(get_token):
    assert get_token.get_specific_folder() is not None


def test_count_succesfull(get_token):
    assert get_token.get_count() is not None


def test_runs_succesfull(get_token):
    assert get_token.get_runs() is not None


def test_analyses_succesfull(get_token):
    assert get_token.get_analyses() is not None


def test_artifacts_succesfull(get_token):
    assert get_token.get_artifacts() is not None
