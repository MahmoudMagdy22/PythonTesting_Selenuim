# conftest.py
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from utils.data_loader import get
from utils.test_utils import TestDataBuilder

@pytest.fixture(scope="session")
def env():
    return get("env")

@pytest.fixture(scope="session")
def routes():
    return get("routes")

@pytest.fixture(scope="session")
def test_data_builder():
    return TestDataBuilder

@pytest.fixture
def setup(env, request):
    browser = env.get("browser", "chrome").lower()
    if browser != "chrome":
        raise RuntimeError("This fixture currently supports only Chrome.")
    
    opts = Options()
    if env.get("headless", False):
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    opts.add_experimental_option("useAutomationExtension", False)
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    try:
        driver = webdriver.Chrome(options=opts)
        driver.set_page_load_timeout(env.get("page_load_timeout", 30))
        driver.implicitly_wait(env.get("implicit_wait", 0))
    except WebDriverException as e:
        pytest.fail(f"Failed to initialize Chrome driver: {e}")
    
    yield driver
    
    # Capture screenshot on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        screenshot_path = screenshot_dir / f"{request.node.name}.png"
        driver.save_screenshot(str(screenshot_path))
        print(f"Screenshot saved: {screenshot_path}")
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
