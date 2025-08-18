# End-to-end authentication test module
# Tests complete user journey from registration to login

# Import required testing framework and page objects
import pytest
from pages.home_page import HomePage  # Page object for home page interactions
from pages.login_page import LoginPage  # Page object for login functionality
from pages.registration_page import RegistrationPage  # Page object for user registration
from utils.data_loader import get  # Utility to load test data from JSON file
from utils.helpers import unique_email  # Helper to generate unique email addresses

@pytest.mark.e2e  # Mark this as an end-to-end test for test categorization
def test_register_then_login(setup, env, routes):
    """Test complete user authentication flow: register new user then login"""
    # Get base URL from environment configuration
    base = env["base_url"]

    # Initialize page objects with WebDriver only (no explicit_wait parameter)
    home = HomePage(setup)  # Home page operations
    login = LoginPage(setup)  # Login page operations
    reg = RegistrationPage(setup)  # Registration page operations

    # Navigate to registration page via login page
    setup.get(base + routes["login"])  # Open login page first
    login.go_to_register()  # Click register link to navigate to registration

    # Prepare test data for new user registration
    defaults = get("registration.defaults")  # Load default registration data from JSON
    import time
    email = f"test{int(time.time())}@example.com"  # Generate unique email
    password = defaults["password"]  # Use default password from test data

    # Perform user registration with individual method calls
    reg.set_gender("male")  # Set gender
    reg.set_names(defaults["first_name"], defaults["last_name"])  # Set names
    reg.set_email(email)  # Set email
    reg.set_password(password)  # Set password
    reg.click_register()  # Submit registration form

    # Verify registration success
    assert "Your registration completed" in setup.page_source
    
    # Handle automatic login after registration - logout to test login separately
    if home.is_logged_in():  # Check if user is automatically logged in
        home.logout()  # Logout to test independent login functionality

    # Test login functionality with newly registered credentials
    home.go_to_login()  # Navigate to login page
    login.login(email, password, remember=True)  # Login with registered credentials and remember me option
    assert home.is_logged_in(), "Expected to be logged in, but logout link was not visible."  # Verify successful login
