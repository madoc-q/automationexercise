from playwright.sync_api import Page, expect 
from config import CART_URL

class CartPage():
    def __init__(self,page:Page):
        self.page = page
        
        
    def open(self):
        self.page.goto(CART_URL)
    
    def proceed_checkout(self):
        self.page.get_by_text('Proceed to Checkout').click()
  
    def remove_product_cart(self, product_number: str = ""):
        if product_number:
            self.page.locator(f'[data-product-id="{product_number}"].cart_quantity_delete').click()
