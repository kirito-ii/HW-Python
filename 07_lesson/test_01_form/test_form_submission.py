import logging
from selenium import webdriver
import pytest
from form_page import FormPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def test_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        form_page = FormPage(driver)

        logger.info("Страница загружена, начинаем заполнять форму")

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

        form_page.submit_form()

        logger.info("Форма успешно отправлена, начинаем валидацию полей")

        zip_code_field = form_page.get_zip_code_field()
        assert "red" in zip_code_field.get_attribute("class"), "Zip code field is not highlighted in red."
        logger.info("Zip code field is correctly highlighted in red.")

        fields = [
            "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
        ]
        for field_name in fields:
            field = form_page.wait_for_element(By.NAME, field_name)
            assert "green" in field.get_attribute("class"), f"{field_name} is not highlighted in green."
            logger.info(f"{field_name} field is correctly highlighted in green.")

    except Exception as e:
        logger.error(f"Test failed due to: {e}")
    finally:
        driver.quit()
        logger.info("Browser closed.")

if __name__ == "__main__":
    pytest.main()
