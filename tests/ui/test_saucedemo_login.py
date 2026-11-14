from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


def test_valid_login(page: Page):
    username = "standard_user"
    password = "secret_sauce"
    
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    
    expect(page).to_have_url(BASE_URL+"/inventory.html")
    
    
def test_invalid_login_shows_error(page: Page):
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("invalid_password")
    page.get_by_role("button", name="Login").click()
    
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("do not match")
    
    