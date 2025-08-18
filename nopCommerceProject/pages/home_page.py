# pages/home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        """Initialize home page with WebDriver only"""
        super().__init__(driver)
    
    LOGIN_LINK = (By.CSS_SELECTOR, "a.ico-login")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a.ico-logout")

    def go_to_login(self) -> None:
        self.click(self.LOGIN_LINK)

    def is_logged_in(self) -> bool:
        # quick presence check (shorter wait)
        return self.is_visible(self.LOGOUT_LINK, timeout=3)

    def logout(self) -> None:
        if self.is_logged_in():
            self.click(self.LOGOUT_LINK)
