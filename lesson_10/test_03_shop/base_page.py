from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Tuple

class BasePage:
    """
    Базовый класс для страниц, обеспечивающий методы для работы с элементами на странице.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация базовой страницы.

        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver

    def wait_for_element(self, by: By, value: str, timeout: int = 10) -> WebDriver:
        """
        Ожидание появления элемента на странице.

        :param by: Локатор элемента.
        :param value: Значение локатора.
        :param timeout: Время ожидания в секундах.
        :return: Веб-элемент, когда он появляется на странице.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_element_to_be_clickable(self, by: By, value: str, timeout: int = 10) -> WebDriver:
        """
        Ожидание, что элемент станет кликабельным.

        :param by: Локатор элемента.
        :param value: Значение локатора.
        :param timeout: Время ожидания в секундах.
        :return: Веб-элемент, когда он становится кликабельным.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def wait_for_element_visibility(self, by: By, value: str, timeout: int = 10) -> WebDriver:
        """
        Ожидание, что элемент станет видимым.

        :param by: Локатор элемента.
        :param value: Значение локатора.
        :param timeout: Время ожидания в секундах.
        :return: Веб-элемент, когда он становится видимым.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
