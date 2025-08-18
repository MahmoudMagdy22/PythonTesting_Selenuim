import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\DELL\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


def test_navigation_url():
    # Maximize the browser window
    driver.maximize_window()
    # Navigate to the login page
    driver.get("http//:demo.nopcommerce.com")
    # Assert that the URL contains the expected substring
  #  assert "rahulshettyacademy" in driver.current_url, "URL does not contain 'rahulshettyacademy'"
    # Wait for 2 seconds to observe the result
    time.sleep(2)


def test_login_page():
    # Enter username in the username field
    driver.find_element("id", "username").send_keys("rahulshettyacademy")
    # Enter password in the password field
    driver.find_element("id", "password").send_keys("learning")
    # Click the sign-in button
    driver.find_element("id", "signInBtn").click()
    # Wait for 5 seconds to allow the page to process login
    time.sleep(5)
    # Switch to the alert and accept it
    assert driver.find_element("xpath", "//a[normalize-space()='iphone X']").is_displayed(), "Element 'iphone X' not found on the page"