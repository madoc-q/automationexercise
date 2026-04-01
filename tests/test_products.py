from playwright.sync_api import expect
from pages.products_page import ProductPage
import re
import pytest

def test_add_product(productspage):
    addcart = ProductPage(productspage)
    addcart.add_product("1")
    expect(productspage.locator(".modal-content")).to_be_visible()
