from behave import *



@Given("login: I am a user on the login_page")
def step_impl(context):
    context.login_page.navigate_to_login_page()

@When('login: I fill in the email field "{e_mail}"')
def step_impl(context, e_mail):
    context.login_page.add_email(e_mail)

@Then('login: I verify the invalid email validation message "{message}"')
def step_impl(context, message):
    context.login_page.verify_the_email_error_message_when_the_email_is_invalid(message)

@Then('login: I  verify the passwor error message "{password_error_message}"')
def step_imp(context, password_error_message):
    context.login_page.verify_password_error(password_error_message)

@Then('login: I verify if the login button is displayed')
def step_imp(context):
    context.login_page.verify_if_the_login_btn_is_displayed()

@When('login: I fill in the password field "{parola}"')
def step_impl(context, parola):
    context.login_page.set_password(parola)

@Then('login: I click on it')
def step_impl(context):
    context.login_page.click_on_login_button()

@When('login: I click on the forgote password link')
def step_impl(context):
    context.login_page.click_on_forgot_password()

@Then('login: I verify if the url its changed')
def step_impl(context):
    context.login_page.verify_url_on_forgot_password_page()