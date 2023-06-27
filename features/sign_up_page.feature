Feature: Check the login page functionality
  
  
    @SignUp1
    Scenario: Check the error from the email field, if we leave the field empty
        Given SignUp: I am as user on Sign Up page
        When SignUp: I click on the Business radio button
        When SignUp: I click on the continue button from the bussines page
        When SignUp: I fill in the field of name business with "Test1"
        When SignUp: I click on the continue button
        When SignUp: I fill in the field of first name with "FirstName"
        When SignUp: I fill in the field of last name with "a"
        Then SignUp: I verify the error message "value can't be empty!"