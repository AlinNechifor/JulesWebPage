Feature: Check the forgot password page functionality
  
  @ForgotPassword1
  Scenario: Check the send button
    Given forgot_password:I am a user on forgot password page
    When forgot_password:I fill in email field "alin@yahoo.com"
    Then forgot_password:I verify if the button is displayed or not
    
  @ForgotPassword2
  Scenario: Check the error message of email field
    Given forgot_password:I am a user on forgot password page
    When forgot_password:I fill in email field "alin"
    Then forgot_password:I check the error message "Please enter a valid email address!"
   
  @ForgotPassword3
  Scenario: Check if the pop-up is displayed when i click on "Send Email" button
    Given forgot_password:I am a user on forgot password page
    When forgot_password:I fill in email field "alisdasdn@yahoo.com"
    When forgot_password:I click on the send email button
    Then forgot_password:I check if the pop up is displayed
    
    
  @ForgotPassword4
  Scenario Outline: Check various email validation
    Given forgot_password:I am a user on forgot password page
    When forgot_password:I fill in email field "<email>"
    When forgot_password:I click on the send email button
    Then forgot_password:I check the error message "<expected_error>"
    
    
    Examples:
      | email           |            expected_error                  |
      | test1           | Please enter a valid email address!        |
      | test2@          | Please enter a valid email address!        |
      | test3@yahoo     | Please enter a valid email address!        |
      | test4@yahoo.com | None                                       |