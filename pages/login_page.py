from playwright.sync_api import Page, expect 
from config import LOGIN_URL

class LoginPage():
    def __init__(self,page:Page):
        self.page=page
        
    def open(self):
        self.page.goto(LOGIN_URL)
        
        
    def login(self,email: str="",password: str=""):
        self.page.locator('[data-qa="login-email"]').fill(email)
        self.page.locator('[data-qa="login-password"]').fill(password)
        self.page.locator('[data-qa="login-button"]').click()
        self.page.wait_for_load_state("load")
        
        