from playwright.sync_api import expect
from pages.signup_page import SignUpPage
import re
import pytest
import uuid


def test_first_signup(first_page):
    first = SignUpPage(first_page)
    unique_email = f"test_{uuid.uuid4()}@example.com"
    first.first_signup("Madoc Quaye", unique_email)
    expect(first_page).to_have_url(re.compile("signup"))


def test_allfields(second_signup_page):
    allfields = SignUpPage(second_signup_page)
    allfields.second_signup(
        title="id_gender1",
        name="Madoc Quaye",
        password="Godisgood",
        firstname="Madoc",
        lastname="Quaye",
        address="Accra",
        country="India",
        state="Greater Accra",
        city="Accra",
        zipcode="233",
        mobilenumber="0244994030",
    )
    expect(second_signup_page).to_have_url(re.compile("account_created"))


@pytest.mark.parametrize(
    "title, name, password, firstname, lastname, address, country, state, city, zipcode, mobilenumber",
    [
        # missing name (required field)
        ("id_gender1", "", "Godisgood", "Madoc", "Quaye", "Accra", "India", "Greater Accra", "Accra", "233", "0244994030"),
        # missing password (required field)
        ("id_gender1", "Madoc Quaye", "", "Madoc", "Quaye", "Accra", "India", "Greater Accra", "Accra", "233", "0244994030"),
        # missing first name (required field)
        ("id_gender1", "Madoc Quaye", "Godisgood", "", "Quaye", "Accra", "India", "Greater Accra", "Accra", "233", "0244994030"),
    ],
)
def test_missing_fields(
    second_signup_page, title, name, password, firstname, lastname, address, country, state, city, zipcode, mobilenumber
):
    missingfields = SignUpPage(second_signup_page)
    missingfields.second_signup(title, name, password, firstname, lastname, address, country, state, city, zipcode, mobilenumber)
    expect(second_signup_page).to_have_url(re.compile("signup"))
