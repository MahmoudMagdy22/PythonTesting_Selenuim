# tests/test_login_negative.py
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_loader import get

@pytest.mark.negative
def test_login_invalid_credentials(setup, env, routes):
    base = env["base_url"]
    home = HomePage(setup, env["explicit_wait"])
    login = LoginPage(setup, env["explicit_wait"])

    home.open(base + routes["login"])
    bad = get("users.invalid")[0]
    login.login(bad["email"], bad["password"])
    assert login.error_present(), "Expected 'Login was unsuccessful' error message."
