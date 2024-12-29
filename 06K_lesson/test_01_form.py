import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def test_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first-name")))

        logger.info("Страница загружена, начинаем заполнять форму")

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "e-mail"))
        )
        email_field.send_keys("test@skypro.com")

        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        logger.info("Форма успешно отправлена, начинаем валидацию полей")

        try:
            zip_code_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "zip-code")))
            assert "red" in zip_code_field.get_attribute("class"), "Zip code field is not highlighted in red."
            logger.info("Zip code field is correctly highlighted in red.")
        except Exception as e:
            logger.error(f"Error during Zip code validation: {e}")
            logger.error(f"HTML of the page at the time of error: {driver.page_source}")

        fields = [
            "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
        ]
        for field_name in fields:
            try:
                field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, field_name)))
                assert "green" in field.get_attribute("class"), f"{field_name} is not highlighted in green."
                logger.info(f"{field_name} field is correctly highlighted in green.")
            except Exception as e:
                logger.error(f"Error during validation for {field_name}: {e}")
                logger.error(f"HTML of the page at the time of error: {driver.page_source}")

    except Exception as e:
        logger.error(f"Test failed due to: {e}")
    finally:
        driver.quit()
        logger.info("Browser closed.")
