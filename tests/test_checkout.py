from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage
import re

def test_checkout(checkoutpage):
    check = CheckoutPage(checkoutpage)
    check.place_order()
    expect(checkoutpage).to_have_url(re.compile('payment'))