from playwright.sync_api import Page, expect 
from config import LOGIN_URL
from config import PRODUCTS_URL


class ProductPage():
    def __init__(self,page:Page):
        self.page = page
        
        
    def open(self):
        self.page.goto(PRODUCTS_URL)
    

    def add_product(self,product_number):
        self.page.locator(f'[data-product-id="{product_number}"].add-to-cart').first.click()