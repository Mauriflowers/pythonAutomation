Feature: Add a product to the cart

 As a common user
    I want to add a product to the cart
    In order to buy a product

Scenario: Adding products to the cart
        Given the user is on Demoblaze page
        When the user add a product to the cart
        Then the cart shows the product inside 