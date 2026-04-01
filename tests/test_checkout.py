from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage
import re
import pytest

def test_checkout(checkoutpage):
    check = CheckoutPage(checkoutpage)
    check.place_order()
    expect(checkoutpage).to_have_url(re.compile('payment'))

def test_full_payment(checkoutpage):
    check = CheckoutPage(checkoutpage)
    check.place_order()
    check.fill_payment(
        name="Madoc Quaye",
        card_number="4111111111111111",
        cvc="123",
        expiry_month="12",
        expiry_year="2027"
    )
    expect(checkoutpage).to_have_url(re.compile("payment_done"))