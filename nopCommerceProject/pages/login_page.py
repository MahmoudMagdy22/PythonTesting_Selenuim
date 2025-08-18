# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        """Initialize login page with WebDriver only"""
        super().__init__(driver)
    
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    REMEMBER = (By.ID, "RememberMe")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    ERROR_SUMMARY = (
        By.CSS_SELECTOR,
        "div.message-error.validation-summary-errors, div.validation-summary-errors",
    )

    # Navigation to registration
    REGISTER_HEADER_LINK = (By.CSS_SELECTOR, "a.ico-register")
    REGISTER_BUTTON_ON_LOGIN = (By.CSS_SELECTOR, "a.register-button, button.register-button, a.button-1.register-button")

    def login(self, email: str, password: str, remember: bool = False) -> None:
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        if remember:
            try:
                checkbox = self.wait.until(lambda d: d.find_element(*self.REMEMBER))
                if not checkbox.is_selected():
                    checkbox.click()
            except Exception:
                # Remember checkbox may not be present in some themes
                pass
        self.click(self.LOGIN_BUTTON)

    def go_to_register(self) -> None:
        # Try reliable header link first; fallback to page button if theme differs
        try:
            self.click(self.REGISTER_HEADER_LINK)
        except TimeoutException:
            self.click(self.REGISTER_BUTTON_ON_LOGIN)

    def error_present(self) -> bool:
        return self.is_visible(self.ERROR_SUMMARY, timeout=3)
