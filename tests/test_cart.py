from playwright.sync_api import expect
from pages.cart_page import CartPage
import re
import pytest


@pytest.mark.parametrize("product_number",
    [
        ("1")
    ]
    
)
def test_remove_cart(cart_page,product_number):
    removecart= CartPage(cart_page)
    removecart.remove_product_cart(product_number)
    expect(cart_page.locator(f'#product-{product_number}')).to_be_hidden()


