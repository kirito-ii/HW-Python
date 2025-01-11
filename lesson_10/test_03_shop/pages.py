from selenium.webdriver.common.by import By
from base_page import BasePage
from typing import Tuple
import allure

class LoginPage(BasePage):
    """
    Страница логина.
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Login with username and password")
    def login(self, username: str, password: str) -> None:
        """
        Выполнение логина.

        :param username: Имя пользователя.
        :param password: Пароль.
        :return: None
        """
        username_input = self.wait_for_element(*self.USERNAME_INPUT)
        password_input = self.wait_for_element(*self.PASSWORD_INPUT)
        login_button = self.wait_for_element_to_be_clickable(*self.LOGIN_BUTTON)

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()


class ProductsPage(BasePage):
    """
    Страница продуктов.
    """

    BACKPACK_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")
    BOLT_TSHIRT_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button")
    ONESIE_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Add Backpack to the cart")
    def add_backpack_to_cart(self) -> None:
        """
        Добавление рюкзака в корзину.

        :return: None
        """
        backpack_button = self.wait_for_element_to_be_clickable(*self.BACKPACK_BUTTON)
        backpack_button.click()

    @allure.step("Add Bolt T-Shirt to the cart")
    def add_bolt_tshirt_to_cart(self) -> None:
        """
        Добавление футболки Bolt в корзину.

        :return: None
        """
        bolt_tshirt_button = self.wait_for_element_to_be_clickable(*self.BOLT_TSHIRT_BUTTON)
        bolt_tshirt_button.click()

    @allure.step("Add Onesie to the cart")
    def add_onesie_to_cart(self) -> None:
        """
        Добавление боди Onesie в корзину.

        :return: None
        """
        onesie_button = self.wait_for_element_to_be_clickable(*self.ONESIE_BUTTON)
        onesie_button.click()

    @allure.step("Go to the cart")
    def go_to_cart(self) -> None:
        """
        Переход в корзину.

        :return: None
        """
        cart_button = self.wait_for_element_to_be_clickable(*self.CART_BUTTON)
        cart_button.click()


class CartPage(BasePage):
    """
    Страница корзины.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Proceed to checkout")
    def proceed_to_checkout(self) -> None:
        """
        Переход к оформлению заказа.

        :return: None
        """
        checkout_button = self.wait_for_element_to_be_clickable(*self.CHECKOUT_BUTTON)
        checkout_button.click()


class CheckoutPage(BasePage):
    """
    Страница оформления заказа.
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUMMARY_TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Fill the checkout form")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнение формы оформления заказа.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param postal_code: Почтовый код.
        :return: None
        """
        first_name_input = self.wait_for_element(*self.FIRST_NAME_INPUT)
        last_name_input = self.wait_for_element(*self.LAST_NAME_INPUT)
        postal_code_input = self.wait_for_element(*self.POSTAL_CODE_INPUT)

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)

    @allure.step("Continue to the summary page")
    def continue_to_summary(self) -> None:
        """
        Переход на страницу с итогами.

        :return: None
        """
        continue_button = self.wait_for_element_to_be_clickable(*self.CONTINUE_BUTTON)
        continue_button.click()

    @allure.step("Get the total price")
    def get_total_price(self) -> str:
        """
        Получение общей стоимости на странице итогов.

        :return: Общая стоимость как строка.
        """
        total_label = self.wait_for_element_visibility(*self.SUMMARY_TOTAL_LABEL)
        return total_label.text
