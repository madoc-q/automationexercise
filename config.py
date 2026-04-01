import os
from dotenv import load_dotenv

BASE_URL = "https://www.automationexercise.com"
LOGIN_URL = f"{BASE_URL}/login"
SIGNUP_URL = f"{BASE_URL}/signup"
CART_URL = f"{BASE_URL}/view-cart"
PRODUCTS_URL = f"{BASE_URL}/products"
CHECKOUT_URL = f"{BASE_URL}/checkout"


# Load the .env file
load_dotenv()


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL")