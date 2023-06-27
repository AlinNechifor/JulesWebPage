from selenium.webdriver import Keys

from browser import Browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class LoginPage(Browser):
    EMAIL_FIELD = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASSWORD_FIELD = (By.XPATH, "//*[@type = 'password']")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button')
    SIGN_UP_BUTTON = (By.XPATH, '//a[@data-test-id= "sign-up-link"]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/a')
    ERROR_MESSAGE_WHEN_THE_EMAIL_IS_INCORRECT = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/p')
    ERROR_MESSAGE_WHEN_THE_PASSWORD_FIELD_IS_EMPTY = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')


    def navigate_to_login_page(self):
        self.driver.get("https://jules.app/sign-in")

    def add_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def verify_the_email_error_message_when_the_email_is_invalid(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_WHEN_THE_EMAIL_IS_INCORRECT).text
        except NoSuchElementException:
            actual_message = 'None'
        assert actual_message == expected_message, f"Error, the message is incorrect"

    def verify_password_error(self, expected_message):
        password = self.driver.find_element(*self.PASSWORD_FIELD)
        password.send_keys("a")
        password.send_keys(Keys.BACK_SPACE)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_WHEN_THE_PASSWORD_FIELD_IS_EMPTY).text
        except NoSuchElementException:
            actual_message = 'None'
        assert actual_message == expected_message, f"Error, the field is not empty"

    def verify_if_the_login_btn_is_displayed(self):
        button = self.driver.find_element(*self.LOGIN_BUTTON)
        assert(button.is_displayed(), f'Element is not displayed')

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_on_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD).click()

    def verify_url_on_forgot_password_page(self):
       actual_url = self.driver.current_url
       expected_url = "https://jules.app/forgot-password"
       assert actual_url == expected_url, f'Invalid url'

    