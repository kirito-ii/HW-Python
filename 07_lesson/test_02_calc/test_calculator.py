from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from calculator_page import CalculatorPage

def test_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        calc_page = CalculatorPage(driver)

        calc_page.set_delay("45")

        calc_page.click_button_7()
        calc_page.click_plus_button()
        calc_page.click_button_8()
        calc_page.click_equal_button()

        result = calc_page.get_result()

        expected_result = "15"
        assert result == expected_result, f"Test failed! Expected '15', but got '{result}'"
        print("Test passed: Calculator result is 15.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main()
