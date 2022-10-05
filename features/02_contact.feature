Feature: Send a Message through the contact button

 As a common user
    I want to use the contact button
    In order to send a message

Scenario: Sending messages through the contact button
        Given the user is on Demoblaze page
        When the user sends a message
        Then the page displays a confirmation message
