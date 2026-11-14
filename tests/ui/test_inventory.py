from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_inventory_shows_six_products(inventory_page: InventoryPage):
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items).to_have_count(6)


def test_add_item_updates_cart_badge(inventory_page: InventoryPage):
    inventory_page.add_to_cart("sauce-labs-backpack")

    expect(inventory_page.cart_badge).to_have_text("1")


def test_logout_returns_to_login_page(page: Page, inventory_page: InventoryPage):
    inventory_page.logout()

    expect(page).to_have_url(LoginPage.URL + "/")