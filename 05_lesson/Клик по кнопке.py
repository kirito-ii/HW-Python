from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

for _ in range(5):
    add_element_button.click()
    time.sleep(1)

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

driver.quit()
