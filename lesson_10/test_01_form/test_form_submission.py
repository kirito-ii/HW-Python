import logging
from selenium import webdriver
import pytest
from form_page import FormPage
from selenium.webdriver.common.by import By
import allure

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@allure.title("Тестирование отправки формы")
@allure.description("Тест заполняет форму и проверяет, что поля подсвечиваются в зависимости от состояния.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission():
    """
    Тестирование отправки формы и валидации ее полей.

    1. Открывает веб-страницу с формой.
    2. Заполняет форму с тестовыми данными.
    3. Отправляет форму.
    4. Проверяет правильность выделения полей формы после отправки (поле "Zip code" и другие поля).
    5. Логирует процесс и результаты валидации.

    Исключения логируются и выводятся в консоль.
    """

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Создание экземпляра страницы формы
        form_page = FormPage(driver)

        with allure.step("Заполняем форму"):
            # Заполнение формы с тестовыми данными
            form_page.fill_form(
                first_name="Иван",
                last_name="Петров",
                address="Ленина, 55-3",
                email="test@skypro.com",
                phone="+7985899998787",
                city="Москва",
                country="Россия",
                job_position="QA",
                company="SkyPro"
            )

        with allure.step("Отправляем форму"):
            # Отправка формы
            form_page.submit_form()

        with allure.step("Валидация поля Zip code"):
            # Проверка выделения поля "Zip code"
            zip_code_field = form_page.get_zip_code_field()
            assert "red" in zip_code_field.get_attribute("class"), "Zip code field is not highlighted in red."
            logger.info("Zip code field is correctly highlighted in red.")

        with allure.step("Валидация других полей"):
            # Валидация других полей
            fields = [
                "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
            ]
            for field_name in fields:
                field = form_page.wait_for_element(By.NAME, field_name)
                assert "green" in field.get_attribute("class"), f"{field_name} is not highlighted in green."
                logger.info(f"{field_name} field is correctly highlighted in green.")

    except Exception as e:
        # Логирование ошибок, если тест не прошел
        logger.error(f"Test failed due to: {e}")
    finally:
        # Закрытие браузера
        driver.quit()
        logger.info("Browser closed.")
