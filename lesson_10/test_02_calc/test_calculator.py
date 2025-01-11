import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    """
    Класс страницы калькулятора.
    Этот класс предоставляет методы для взаимодействия с элементами на странице калькулятора.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр WebDriver для работы с браузером.
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "input#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equal = (By.XPATH, "//span[text()='=']")

    def set_delay(self, delay_time: int) -> None:
        """
        Устанавливает задержку для калькулятора.

        :param delay_time: Задержка в секундах (целое число).
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_time))

    def click_button(self, button_locator: tuple) -> None:
        """
        Нажимает кнопку на калькуляторе.

        :param button_locator: Локатор кнопки (кортеж, состоящий из типа локатора и значения).
        """
        self.driver.find_element(*button_locator).click()

    def get_result(self) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        :return: Результат вычисления как строка.
        """
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, result: str, timeout: int = 50) -> None:
        """
        Ожидает появления нужного результата на экране калькулятора.

        :param result: Ожидаемый результат (строка).
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, result)
        )


@pytest.fixture
def setup():
    """
    Фикстура для настройки теста. Создает драйвер, открывает страницу калькулятора.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@allure.title("Тест калькулятора")
@allure.description("Тестирование калькулятора для проверки правильности вычислений с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(setup):
    """
    Тест для калькулятора, проверяющий выполнение операций с задержкой.
    """
    driver = setup
    calculator_page = CalculatorPage(driver)

    with allure.step("Устанавливаем задержку в 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Нажимаем кнопки 7, +, 8 и ="):
        calculator_page.click_button(calculator_page.button_7)
        calculator_page.click_button(calculator_page.button_plus)
        calculator_page.click_button(calculator_page.button_8)
        calculator_page.click_button(calculator_page.button_equal)

    with allure.step("Ожидаем, пока результат появится"):
        calculator_page.wait_for_result("15")

    with allure.step("Проверяем результат вычисления"):
        result = calculator_page.get_result()
        assert int(result) == 15
