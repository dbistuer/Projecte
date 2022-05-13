Feature: Register client
  In order to create a new account
  As a user or a non-registered user
  I want to register a new client with its details

Scenario: Register succesfully a new client
    When I register client
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   patata        |   1234            |   ES9121000418450200051332    |
    Then I'm viewing the login page
    And there's a new client with the previous data

Scenario: Register a new client with invalid values
    When I register a client with wrong information
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   1234   |   Carrer      |   1234       |   m@hotmail.com   |   patata        |   1234            |   1234    |
      Then I'm able to see an error message
      Then I can click a link that takes me back to the register page
      And The client doesn't exist
