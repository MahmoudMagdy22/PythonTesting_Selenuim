# Registration page object - handles all registration form interactions
# Constructor only accepts WebDriver instance, no base_url needed

from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        """Initialize registration page with WebDriver only"""
        super().__init__(driver)  # Initialize BasePage with driver
        
        # Define all page element locators
        self.gender_male_radio = (By.ID, "gender-male")  # Male gender radio button
        self.gender_female_radio = (By.ID, "gender-female")  # Female gender radio button
        self.first_name_input = (By.ID, "FirstName")  # First name input field
        self.last_name_input = (By.ID, "LastName")  # Last name input field
        self.email_input = (By.ID, "Email")  # Email input field
        self.password_input = (By.ID, "Password")  # Password input field
        self.confirm_password_input = (By.ID, "ConfirmPassword")  # Confirm password input field
        self.register_button = (By.ID, "register-button")  # Register submit button
        self.result_message = (By.CLASS_NAME, "result")  # Success/error message element

    def set_gender(self, gender="male"):
        """Select gender radio button - male or female"""
        if gender.lower() == "male":
            self.click(self.gender_male_radio)  # Click male radio button
        else:
            self.click(self.gender_female_radio)  # Click female radio button

    def set_names(self, first_name, last_name):
        """Enter first name and last name in respective input fields"""
        # Clear and enter first name
        self.type(self.first_name_input, first_name)
        # Clear and enter last name
        self.type(self.last_name_input, last_name)

    def set_email(self, email):
        """Enter email address in email input field"""
        self.type(self.email_input, email)  # Enter email

    def set_password(self, password):
        """Enter password in both password and confirm password fields"""
        # Enter password in password field
        self.type(self.password_input, password)
        # Enter same password in confirm password field
        self.type(self.confirm_password_input, password)

    def click_register(self):
        """Click the register button to submit the registration form"""
        self.click(self.register_button)

    def get_result_message(self):
        """Get the result message text after registration attempt"""
        return self.text_of(self.result_message)  # Return message text
