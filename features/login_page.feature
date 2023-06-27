Feature: Check the login page functionality

    @login1
    Scenario: Check validation error message when email is invalid format
        Given login: I am a user on the login_page
        When login: I fill in the email field "my_email12@"
        Then login: I verify the invalid email validation message "Please enter a valid email address!"
        
    @login2
    Scenario: Check validation error message when password field is empty
        Given login: I am a user on the login_page
        When login: I fill in the email field "my_email12@yahoo.com"
        Then login: I  verify the passwor error message "Please enter your password!"
        Then login: I verify if the login button is displayed
        
    @login3
    Scenario: Check if the log in button is available by filling in the email and password fields
        Given login: I am a user on the login_page
        When login: I fill in the email field "my_email12@yahoo.com"
        When login: I fill in the password field "parola"
        Then login: I verify if the login button is displayed
        Then login: I click on it
    
    @login4
    Scenario: I check if i click on forgot password link it will change its url
        Given login: I am a user on the login_page
        When login: I click on the forgote password link
        Then login: I verify if the url its changed
        