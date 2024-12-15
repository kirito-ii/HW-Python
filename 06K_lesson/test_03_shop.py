from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome()


def test_shopping_cart():
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

    backpack_button = driver.find_element(By.XPATH,
                                          "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")
    backpack_button.click()

    bolt_tshirt_button = driver.find_element(By.XPATH,
                                             "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button")
    bolt_tshirt_button.click()

    onesie_button = driver.find_element(By.XPATH,
                                        "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
    onesie_button.click()

    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    postal_code_input.send_keys("12345")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))

    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    assert total_price == "Total: $58.29", f"Expected Total: $58.29, but got {total_price}"

    driver.quit()


if __name__ == "__main__":
    pytest.main()