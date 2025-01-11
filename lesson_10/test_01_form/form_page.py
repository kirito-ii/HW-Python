from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement  # Импортируем WebElement

class FormPage(BasePage):
    """
    Класс FormPage расширяет BasePage и предоставляет методы для взаимодействия с формой на веб-странице.

    Атрибуты:
        FIRST_NAME_FIELD (tuple): Локатор для поля "Имя".
        LAST_NAME_FIELD (tuple): Локатор для поля "Фамилия".
        ADDRESS_FIELD (tuple): Локатор для поля "Адрес".
        EMAIL_FIELD (tuple): Локатор для поля "Электронная почта".
        PHONE_FIELD (tuple): Локатор для поля "Телефон".
        CITY_FIELD (tuple): Локатор для поля "Город".
        COUNTRY_FIELD (tuple): Локатор для поля "Страна".
        JOB_POSITION_FIELD (tuple): Локатор для поля "Должность".
        COMPANY_FIELD (tuple): Локатор для поля "Компания".
        ZIP_CODE_FIELD (tuple): Локатор для поля "Почтовый индекс".
        SUBMIT_BUTTON (tuple): Локатор для кнопки отправки формы.
    """

    FIRST_NAME_FIELD = (By.NAME, "first-name")
    LAST_NAME_FIELD = (By.NAME, "last-name")
    ADDRESS_FIELD = (By.NAME, "address")
    EMAIL_FIELD = (By.NAME, "e-mail")
    PHONE_FIELD = (By.NAME, "phone")
    CITY_FIELD = (By.NAME, "city")
    COUNTRY_FIELD = (By.NAME, "country")
    JOB_POSITION_FIELD = (By.NAME, "job-position")
    COMPANY_FIELD = (By.NAME, "company")
    ZIP_CODE_FIELD = (By.NAME, "zip-code")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_form(self, first_name: str, last_name: str, address: str, email: str,
                  phone: str, city: str, country: str, job_position: str, company: str):
        """
        Заполняет форму на странице.

        Параметры:
            first_name (str): Имя пользователя.
            last_name (str): Фамилия пользователя.
            address (str): Адрес пользователя.
            email (str): Электронная почта пользователя.
            phone (str): Телефон пользователя.
            city (str): Город пользователя.
            country (str): Страна пользователя.
            job_position (str): Должность пользователя.
            company (str): Компания пользователя.
        """
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.CITY_FIELD).send_keys(city)
        self.driver.find_element(*self.COUNTRY_FIELD).send_keys(country)
        self.driver.find_element(*self.JOB_POSITION_FIELD).send_keys(job_position)
        self.driver.find_element(*self.COMPANY_FIELD).send_keys(company)

    def submit_form(self) -> None:
        """
        Отправляет форму на странице, нажимая на кнопку отправки.

        Возвращает:
            None
        """
        submit_button = self.wait_for_element_to_be_clickable(*self.SUBMIT_BUTTON)
        submit_button.click()

    def get_zip_code_field(self) -> WebElement:
        """
        Получает поле для ввода почтового индекса.

        Возвращает:
            WebElement: Элемент поля "Почтовый индекс".
        """
        return self.wait_for_element(*self.ZIP_CODE_FIELD)
