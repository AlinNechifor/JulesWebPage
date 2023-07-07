Feature: Check the login page functionality
  
  
    @SignUp1
    Scenario: Check the error from the email field, if we leave the field empty
        Given SignUp: I am as user on Sign Up page
        When SignUp: I click on the personal radio button
        When SignUp: I click on the continue button from the personal page
        When SignUp: I fill in the field of first name with "FirstName"
        When SignUp: I click on the continue button
        When SignUp: I fill in the field of last name with "a"
        When SignUp: I click on the continue button
        Then SignUp: I verify the error message "value can't be empty!"