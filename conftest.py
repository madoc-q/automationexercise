import pytest
from pages.signup_page import SignUpPage


@pytest.fixture
def first_page(page):
    signup = SignUpPage(page)
    signup.open()
    return page


@pytest.fixture
def second_signup_page(first_page):
    signup = SignUpPage(first_page)
    signup.first_signup("Madoc Quaye", "quaye.madoc@gmail.com")
    return first_page
