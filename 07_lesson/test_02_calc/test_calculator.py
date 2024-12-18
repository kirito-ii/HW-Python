import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Класс страницы калькулятора
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "input#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equal = (By.XPATH, "//span[text()='=']")

    def set_delay(self, delay_time):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_time))

    def click_button(self, button_locator):
        self.driver.find_element(*button_locator).click()

    def get_result(self):
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, result, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, result)
        )


# Тест калькулятора
@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(setup):
    driver = setup
    calculator_page = CalculatorPage(driver)

    # Устанавливаем задержку
    calculator_page.set_delay(45)

    # Нажимаем кнопки 7, +, 8 и =
    calculator_page.click_button(calculator_page.button_7)
    calculator_page.click_button(calculator_page.button_plus)
    calculator_page.click_button(calculator_page.button_8)
    calculator_page.click_button(calculator_page.button_equal)

    # Ждем, пока результат появится
    calculator_page.wait_for_result("15")

    # Проверяем, что результат правильный
    result = calculator_page.get_result()
    assert int(result) == 15
