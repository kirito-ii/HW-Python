from selenium.webdriver.common.by import By
from base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUMMARY_TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_input = self.wait_for_element(*self.FIRST_NAME_INPUT)
        last_name_input = self.wait_for_element(*self.LAST_NAME_INPUT)
        postal_code_input = self.wait_for_element(*self.POSTAL_CODE_INPUT)

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)

    def continue_to_summary(self):
        continue_button = self.wait_for_element_to_be_clickable(*self.CONTINUE_BUTTON)
        continue_button.click()

    def get_total_price(self):
        total_label = self.wait_for_element_visibility(*self.SUMMARY_TOTAL_LABEL)
        return total_label.text
