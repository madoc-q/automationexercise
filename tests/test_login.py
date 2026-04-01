from playwright.sync_api import Page, expect 
from pages.signup_page import SignUpPage
import pytest
import re
from pages.login_page import LoginPage
from config import BASE_URL

def test_successfullogin(firstlogged_in_page):
    logged= LoginPage(firstlogged_in_page)
    logged.login("quaye.madoc@gmail.com","Godisgood")
    expect(firstlogged_in_page).to_have_url(re.compile("automationexercise.com"))
    
    
@pytest.mark.parametrize(
    "email,password",
    [
    ("quaye.madoc@gmail.com","Godisgood"), #wrong email, correct password
    ("",""), #blank field
    ("quaye.madoc@gmail.com","jsss") #correct email, wrong p
]
)

def test_login_missingfields(firstlogged_in_page,email,password):
    missingfields= LoginPage(firstlogged_in_page)
    missingfields.login(email,password)
    
    