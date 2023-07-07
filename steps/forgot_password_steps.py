from behave import *

@Given("forgot_password:I am a user on forgot password page")
def step_impl(context):
    context.forgot_password_page.navigate_to_forgot_password_page()

@When('forgot_password:I fill in email field "{email}"')
def step_impl(context, email):
    context.forgot_password_page.fill_in_email_field(email)

@then('forgot_password:I verify if the button is displayed or not')
def step_impl(context):
    context.forgot_password_page.verify_if_the_send_email_button_is_displayed()

@then('forgot_password:I check the error message "{error_message}"')
def step_impl(context, error_message):
    context.forgot_password_page.verify_the_error_message(error_message)

@when('forgot_password:I click on the send email button')
def step_impl(context):
    context.forgot_password_page.press_send_email_button()

@then('forgot_password:I check if the pop up is displayed')
def step_impl(context):
    context.forgot_password_page.verify_the_pop_up_is_displayed()
