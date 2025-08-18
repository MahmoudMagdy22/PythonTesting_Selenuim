# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple

Locator = Tuple[str, str]

class BasePage:
    def __init__(self, driver: WebDriver, wait_timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Locator, text: str, clear: bool = True) -> None:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text)

    def is_visible(self, locator: Locator, timeout: int | None = None) -> bool:
        try:
            (self.wait if timeout is None else WebDriverWait(self.driver, timeout)).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def text_of(self, locator: Locator) -> str:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text
