from playwright.sync_api import Page  #import page from playwright


#create a blueprint for the invenoty page
class InventoryPage:
    
    #prepare the InventoryPage object
    def __init__(self, page: Page):
        
        #save the browser page
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        #find the shopping cart number
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")


    #add an item to the cart
    def add_to_cart(self, product_slug: str):
        
        #click the add to cart button for the product with the given slug
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()