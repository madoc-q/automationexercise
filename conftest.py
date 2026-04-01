import pytest
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from playwright.sync_api import Page, expect 
from pages.signup_page import SignUpPage
from pages.cart_page import CartPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
from config import USERNAME, PASSWORD
import os 


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")

@pytest.fixture
def first_page(page):
    firstsignup = SignUpPage(page)
    firstsignup.open()
    return page


@pytest.fixture
def second_signup_page(first_page):
    secondsignup = SignUpPage(first_page)
    secondsignup.first_signup("Madoc Quaye", "quaye.madoc@gmail.com")
    return first_page


@pytest.fixture
def firstlogged_in_page(page):
    floggedin= LoginPage(page)
    floggedin.open()
    #loggedin.login('quaye.madoc@gmail.com','Godisgood')
    return page

@pytest.fixture
def logged_in_page(page):
     loggedin= LoginPage(page)
     loggedin.open()
     loggedin.login(USERNAME,PASSWORD)
     return page

@pytest.fixture
def productspage(logged_in_page):
    products= ProductPage(logged_in_page)
    products.open()
    return logged_in_page

# @pytest.fixture
# def cart_page(productspage):
#     products = ProductPage(productspage)
#     products.add_product("1")
#     #productspage.locator('a[href="/view_cart"]').first.click()
#     productspage.get_by_text('View Cart').click()
#     return productspage

# @pytest.fixture
# def proceed_checkoutpage(cart_page):
#     checko= CartPage(cart_page)
#     checko.open()
#     cart_page.get_by_text('Proceed To Checkout').click()
#     return cart_page
    
# @pytest.fixture
# def checkoutpage(proceed_checkoutpage):
#     checkk = CheckoutPage(proceed_checkoutpage)
#     checkk.open()
#     return proceed_checkoutpage
    
@pytest.fixture
def cart_page(productspage):
    products = ProductPage(productspage)
    products.add_product("1")
    productspage.get_by_text('View Cart').click()# more reliable than get_by_text
    return productspage

@pytest.fixture
def proceed_checkoutpage(cart_page):
    # don't call open() — we're already on cart page
    cart_page.get_by_text('Proceed To Checkout').click()# more reliable than get_by_text
    return cart_page

@pytest.fixture
def checkoutpage(proceed_checkoutpage):
    # don't call open() — we're already on checkout page
    return proceed_checkoutpage