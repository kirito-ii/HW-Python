from selenium.webdriver.common.by import By
from base_page import BasePage

class CalculatorPage(BasePage):
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    PLUS_BUTTON = (By.XPATH, "//span[text()='+']")
    EQUAL_BUTTON = (By.XPATH, "//span[text()='=']")
    RESULT = (By.ID, "result")

    def set_delay(self, delay):
        delay_input = self.wait_for_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button_7(self):
        button_7 = self.wait_for_element_to_be_clickable(*self.BUTTON_7)
        button_7.click()

    def click_button_8(self):
        button_8 = self.wait_for_element_to_be_clickable(*self.BUTTON_8)
        button_8.click()

    def click_plus_button(self):
        plus_button = self.wait_for_element_to_be_clickable(*self.PLUS_BUTTON)
        plus_button.click()

    def click_equal_button(self):
        equal_button = self.wait_for_element_to_be_clickable(*self.EQUAL_BUTTON)
        equal_button.click()

    def get_result(self):
        result = self.wait_for_element_visibility(*self.RESULT)
        return result.text