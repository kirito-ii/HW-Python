from selenium.webdriver.common.by import By
from base_page import BasePage

class FormPage(BasePage):
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

    def fill_form(self, first_name, last_name, address, email, phone, city, country, job_position, company):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.CITY_FIELD).send_keys(city)
        self.driver.find_element(*self.COUNTRY_FIELD).send_keys(country)
        self.driver.find_element(*self.JOB_POSITION_FIELD).send_keys(job_position)
        self.driver.find_element(*self.COMPANY_FIELD).send_keys(company)

    def submit_form(self):
        submit_button = self.wait_for_element_to_be_clickable(*self.SUBMIT_BUTTON)
        submit_button.click()

    def get_zip_code_field(self):
        return self.wait_for_element(*self.ZIP_CODE_FIELD)
