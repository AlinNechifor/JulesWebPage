from selenium.webdriver import Keys

from browser import Browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ForgotPassword(Browser):
    EMAIL_FIELD = (By.TAG_NAME, 'input')
    SEND_EMAIL_BUTTON = (By.XPATH, '//button[@type="button"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/p')
    POP_UP = (By.XPATH, '//*[@id="root"]/div/div[2]/div')
    TEXT_FROM_THE_POP_UP = (By.XPATH, '//*[@id="root"]/div/div[2]/div')

    def navigate_to_forgot_password_page(self):
        self.driver.get("https://jules.app/forgot-password")

    def fill_in_email_field(self, text):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(text)

    def press_send_email_button(self):
        try:
            button = self.driver.find_element(*self.SEND_EMAIL_BUTTON)
            if button.is_displayed():
                self.driver.execute_script("arguments[0].click();", button)
            else:
                print("Button is not displayed")
        except NoSuchElementException:
            print("Button not found")

    def verify_if_the_send_email_button_is_displayed(self):
        button = self.driver.find_element(*self.SEND_EMAIL_BUTTON)
        assert button.is_displayed(), "Button is not displayed"

    def verify_the_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, f"The error is not {actual_message}"

    def verify_the_pop_up_is_displayed(self):
        try:
            actual_pop_up = self.driver.find_element(*self.POP_UP)
        except NoSuchElementException:
            actual_pop_up = 'None'
        assert actual_pop_up.is_displayed(), f'The pop up is not displayed'
