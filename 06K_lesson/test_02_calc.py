from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        button_7 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
        )
        button_7.click()

        plus_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        )
        plus_button.click()

        button_8 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
        )
        button_8.click()

        equal_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        )
        equal_button.click()

        result = WebDriverWait(driver, 45).until(
            EC.visibility_of_element_located((By.ID, "result"))
        )

        expected_result = "15"

        assert result.text == expected_result, f"Test failed! Expected '15', but got '{result.text}'"
        print("Test passed: Calculator result is 15.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_calculator()
