from selenium.webdriver import Keys

from browser import Browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''
Pagina Web crapa odata ce ajungem pe pagina cu LAST_NAME, citeste la Reportul " 4.html" (explicatie mai lunga) sau citeste explicatia de mai jos (explicatia mai scurta).
    - crapa deoare ce un element web pe care încercați să îl manipulați nu mai este în starea dorită sau nu mai este atașat la DOM-ul paginii. 
Acest lucru poate fi cauzat de schimbări în DOM sau de actualizări ale paginii care duc la invalidarea referinței elementului.
'''
class SignUpPage(Browser):
    Radio_Button_Business = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[1]/label/span[1]/span/input')
    CONTINUE_BUTTON_AFTER_I_SELECT_ON_OF_THE_RADIO_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button')
    UNIVERSAL_CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')  #acest button de "Continue" se foloseste pe toate paginile, mai putine pe prima pagina unde selectam in ce scop ne facem contul (daca este business sau personal)
    NAME_OF_YOUR_BUSINESS_FIELD = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    LAST_NAME_FIELD = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    ERROR_WHO_APPEAR_IF_WE_LEAVE_EMAIL_FIELD_EMPTY = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')


    def navigate_to_sign_up_page(self):
        self.driver.get('https://jules.app/sign-up')

    def click_on_radio_business_button(self):
        self.driver.find_element(*self.Radio_Button_Business).click()

    def click_on_continue_button_after_i_select_the_radio_business_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON_AFTER_I_SELECT_ON_OF_THE_RADIO_BUTTON).click()

    def fill_in_the_field_name_of_business(self, name_of_business):
        self.driver.find_element(*self.NAME_OF_YOUR_BUSINESS_FIELD).send_keys(name_of_business)

    def click_on_universal_continue_button(self):
        self.driver.find_element(*self.UNIVERSAL_CONTINUE_BUTTON).click()

    def fill_in_the_field_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

    def fill_in_the_field_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def fill_in_the_field_email_address(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def verify_the_error_that_appeared_if_i_leave_the_email_field_empty(self, expected_message):
        email = self.driver.find_element()
        email.send_keys("a")
        email.send_keys(Keys.BACK_SPACE)
        try:
            actual_message = self.driver.find_element(*self.ERROR_WHO_APPEAR_IF_WE_LEAVE_EMAIL_FIELD_EMPTY).text
        except NoSuchElementException:
            actual_message = 'None'
        assert actual_message == expected_message, "Error, field is not empty"














