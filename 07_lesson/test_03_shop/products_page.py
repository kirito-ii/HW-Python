from selenium.webdriver.common.by import By
from base_page import BasePage

class ProductsPage(BasePage):
    BACKPACK_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")
    BOLT_TSHIRT_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button")
    ONESIE_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        backpack_button = self.wait_for_element_to_be_clickable(*self.BACKPACK_BUTTON)
        backpack_button.click()

    def add_bolt_tshirt_to_cart(self):
        bolt_tshirt_button = self.wait_for_element_to_be_clickable(*self.BOLT_TSHIRT_BUTTON)
        bolt_tshirt_button.click()

    def add_onesie_to_cart(self):
        onesie_button = self.wait_for_element_to_be_clickable(*self.ONESIE_BUTTON)
        onesie_button.click()

    def go_to_cart(self):
        cart_button = self.wait_for_element_to_be_clickable(*self.CART_BUTTON)
        cart_button.click()
