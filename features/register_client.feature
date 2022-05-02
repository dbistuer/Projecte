Feature: Register client
  In order to create a new account
  As a user or a non-registered user
  I want to register a new client with its details

Scenario: Register a new client
    When I register client
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   marc        |   1234            |   ES9121000418450200051332    |
    Then I'm viewing the login page
    And there's a new client with the previous data

