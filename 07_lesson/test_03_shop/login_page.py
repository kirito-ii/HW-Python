from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        username_input = self.wait_for_element(*self.USERNAME_INPUT)
        password_input = self.wait_for_element(*self.PASSWORD_INPUT)
        login_button = self.wait_for_element_to_be_clickable(*self.LOGIN_BUTTON)

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
