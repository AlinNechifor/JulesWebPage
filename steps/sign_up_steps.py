from behave import *

@Given('SignUp: I am as user on Sign Up page')
def step_imp(context):
    context.sign_up_page.navigate_to_sign_up_page()

@When('SignUp: I click on the Business radio button')
def step_impl(context):
    context.sign_up_page.click_on_radio_business_button()

@When('SignUp: I click on the continue button from the bussines page')
def step_impl(context):
    context.sign_up_page.click_on_continue_button_after_i_select_the_radio_business_button()

@When('SignUp: I fill in the field of name business with "{name_of_business}"')
def step_impl(context, name_of_business):
    context.sign_up_page.fill_in_the_field_name_of_business(name_of_business)

@When('SignUp: I click on the continue button')
def step_impl(context):
    context.sign_up_page.click_on_universal_continue_button()

@When('SignUp: I fill in the field of first name with "{first_name}"')
def step_impl(context, first_name):
    context.sign_up_page.fill_in_the_field_first_name(first_name)

@When('SignUp: I fill in the field of last name with "{last_name}"')
def step_impl(context, last_name):
    context.sign_up_page.fill_in_the_field_last_name(last_name)

@Then('SignUp: I verify the error message "{error_message}"')
def step_impl(context, error_message):
    context.sign_up_page.verify_the_error_that_appeared_if_i_leave_the_email_field_empty(error_message)