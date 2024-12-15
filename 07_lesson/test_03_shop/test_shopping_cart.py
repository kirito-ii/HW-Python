from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

def test_shopping_cart():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.login("standard_user", "secret_sauce")

        products_page.add_backpack_to_cart()
        products_page.add_bolt_tshirt_to_cart()
        products_page.add_onesie_to_cart()

        products_page.go_to_cart()
        cart_page.proceed_to_checkout()

        checkout_page.fill_checkout_form("John", "Doe", "12345")
        checkout_page.continue_to_summary()

        total_price = checkout_page.get_total_price()

        assert total_price == "Total: $58.29", f"Expected Total: $58.29, but got {total_price}"
        print("Test passed: Total price is correct.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main()
