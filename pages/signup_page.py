from playwright.sync_api import Page
from config import LOGIN_URL


class SignUpPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(LOGIN_URL)
        

    def first_signup(self, name: str, email: str):
        self.page.locator('[data-qa="signup-name"]').fill(name)
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.locator('[data-qa="signup-button"]').click()

    def second_signup(
        self,
        title: str = "",
        name: str = "",
        password: str = "",
        firstname: str = "",
        lastname: str = "",
        address: str = "",
        country: str = "",
        state: str = "",
        city: str = "",
        zipcode: str = "",
        mobilenumber: str = "",
    ):
        # only select title radio if provided
        if title:
            self.page.locator(f"#{title}").check()
        self.page.locator('[data-qa="name"]').fill(name)
        self.page.locator('[data-qa="password"]').fill(password)
        self.page.locator('[data-qa="first_name"]').fill(firstname)
        self.page.locator('[data-qa="last_name"]').fill(lastname)
        self.page.locator('[data-qa="address"]').fill(address)
        self.page.locator('[data-qa="country"]').select_option(country)
        self.page.locator('[data-qa="state"]').fill(state)
        self.page.locator('[data-qa="city"]').fill(city)
        self.page.locator('[data-qa="zipcode"]').fill(zipcode)
        self.page.locator('[data-qa="mobile_number"]').fill(mobilenumber)
        self.page.locator('[data-qa="create-account"]').click()
