from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
)
blue_button.click()

green_banner = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)

banner_text = green_banner.text

print(banner_text)

driver.quit()
