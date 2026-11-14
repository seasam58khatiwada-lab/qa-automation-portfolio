import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"

INVALID_LOGINS = [
    ("standard_user", "wrong_password", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
]


def test_valid_login(page: Page):
    username = "standard_user"
    password = "secret_sauce"

    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(BASE_URL + "/inventory.html")


@pytest.mark.parametrize("username, password, expected_error", INVALID_LOGINS)
def test_invalid_login_shows_error(page: Page, username, password, expected_error):
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text(expected_error)