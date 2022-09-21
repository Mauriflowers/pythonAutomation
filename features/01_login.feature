Feature: Login to Demoblaze

 As a common user
    I want to Login
    In order to have access to the application

Scenario: Login with valid credentials
        Given the user is on Demoblaze page
        When the user logs in with valid credentials
        Then the page shows the log out button 
        Then the page shows the welcome button