from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement  # Импортируем WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Класс BasePage предоставляет общие методы для работы с веб-страницей.
    Этот класс является базовым для страниц, с которыми будет взаимодействовать тест.

    Атрибуты:
        driver (webdriver): Экземпляр WebDriver, который используется для взаимодействия с веб-страницей.
    """

    def __init__(self, driver: webdriver.Chrome):
        """
        Конструктор инициализирует экземпляр BasePage.

        Параметры:
            driver (webdriver.Chrome): Экземпляр WebDriver.
        """
        self.driver = driver

    def wait_for_element(self, by: By, value: str, timeout: int = 10) -> WebElement:
        """
        Ожидает появления элемента на странице.

        Параметры:
            by (By): Метод поиска элемента (например, By.ID, By.NAME и т.д.).
            value (str): Значение для поиска элемента.
            timeout (int): Время ожидания (по умолчанию 10 секунд).

        Возвращает:
            WebElement: Элемент, который был найден на странице.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by: By, value: str, timeout: int = 10) -> WebElement:
        """
        Ожидает, пока элемент станет доступен для клика.

        Параметры:
            by (By): Метод поиска элемента.
            value (str): Значение для поиска элемента.
            timeout (int): Время ожидания (по умолчанию 10 секунд).

        Возвращает:
            WebElement: Кликабельный элемент на странице.
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
