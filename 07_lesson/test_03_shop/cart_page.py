from selenium.webdriver.common.by import By
from base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        checkout_button = self.wait_for_element_to_be_clickable(*self.CHECKOUT_BUTTON)
        checkout_button.click()
