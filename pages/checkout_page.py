from playwright.sync_api import Page
from config import CHECKOUT_URL

class CheckoutPage():
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(CHECKOUT_URL)

    def place_order(self):
        self.page.locator('a[href="/payment"]').click()

    def fill_payment(self, name: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str):
        self.page.locator('[data-qa="name-on-card"]').fill(name)
        self.page.locator('[data-qa="card-number"]').fill(card_number)
        self.page.locator('[data-qa="cvc"]').fill(cvc)
        self.page.locator('[data-qa="expiry-month"]').fill(expiry_month)
        self.page.locator('[data-qa="expiry-year"]').fill(expiry_year)
        self.page.locator('[data-qa="pay-button"]').click()