from playwright.sync_api import Page
from config import CHECKOUT_URL

class CheckoutPage():
    def __init__(self, page):  # fix: __innit__ → __init__
        self.page = page
        
    def open(self):
        self.page.goto(CHECKOUT_URL)
        
    def place_order(self):
        self.page.get_by_text('Place Order').click()  # fix: .click.click() → .click()
        
    
    
    