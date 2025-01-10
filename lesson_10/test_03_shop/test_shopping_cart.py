import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pages import LoginPage, ProductsPage, CartPage, CheckoutPage

@allure.title("Shopping Cart Test")
@allure.description("This test validates the checkout process in the shopping cart")
@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.NORMAL)
def test_shopping_cart():
    """
    Тестовый сценарий для проверки оформления заказа в корзине.

    :return: None
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Log in with valid credentials"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Add items to the cart"):
            products_page.add_backpack_to_cart()
            products_page.add_bolt_tshirt_to_cart()
            products_page.add_onesie_to_cart()

        with allure.step("Go to cart and proceed to checkout"):
            products_page.go_to_cart()
            cart_page.proceed_to_checkout()

        with allure.step("Fill the checkout form"):
            checkout_page.fill_checkout_form("John", "Doe", "12345")

        with allure.step("Continue to summary page"):
            checkout_page.continue_to_summary()

        with allure.step("Verify the total price"):
            total_price = checkout_page.get_total_price()
            assert total_price == "Total: $58.29", f"Expected Total: $58.29, but got {total_price}"

    except Exception as e:
        allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed: {e}")

    finally:
        driver.quit()
