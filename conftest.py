import pytest
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
from config import USERNAME, PASSWORD
import os
import uuid


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
    page.wait_for_selector('[data-qa="signup-name"]', state="visible", timeout=10000)
    return page


@pytest.fixture
def firstlogged_in_page(page):
    floggedin = LoginPage(page)
    floggedin.open()
    page.wait_for_selector('[data-qa="login-email"]', state="visible", timeout=10000)
    return page


@pytest.fixture
def second_signup_page(first_page):
    secondsignup = SignUpPage(first_page)
    unique_email = f"test_{uuid.uuid4()}@example.com"
    secondsignup.first_signup("Madoc Quaye", unique_email)
    first_page.wait_for_selector('[data-qa="name"]', state="visible", timeout=10000)
    return first_page


@pytest.fixture
def logged_in_page(page):
    loggedin = LoginPage(page)
    loggedin.open()
    page.wait_for_selector('[data-qa="login-email"]', state="visible", timeout=10000)
    loggedin.login(USERNAME, PASSWORD)
    return page


@pytest.fixture
def productspage(logged_in_page):
    products = ProductPage(logged_in_page)
    products.open()
    return logged_in_page


@pytest.fixture
def cart_page(productspage):
    products = ProductPage(productspage)
    products.add_product("1")
    productspage.get_by_text('View Cart').click()
    return productspage


@pytest.fixture
def proceed_checkoutpage(cart_page):
    cart_page.get_by_text('Proceed To Checkout').click()
    return cart_page


@pytest.fixture
def checkoutpage(proceed_checkoutpage):
    return proceed_checkoutpage


@pytest.fixture
def checkout_page(cart_page):
    cart_page.locator('a[href="/checkout"]').click()
    return cart_page


@pytest.fixture
def mobile_page(playwright):
    iphone = playwright.devices["iPhone 13"]
    browser = playwright.chromium.launch()
    context = browser.new_context(**iphone)
    page = context.new_page()
    yield page
    browser.close()