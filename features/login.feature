Feature: Login
  In order to acceess pages that require registration
  As a user or a non-registered user
  I want to login

Background: There is a registered user
    Given Exists a user "marc" with password "1234"
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   marc        |   1234            |   ES9121000418450200051332    |

Scenario: Login succesfully 
    When I login as "marc" with password "1234"
    |   username       |   password        | 
    |   marc        |   1234            |
    Then I'm viewing the home page
    And The user "marc" has logged succesfully

Scenario: Login failed
    When I login with a user that is not registered
    |   username       |   password        | 
    |   marc           |   wrongPassword            |
    Then I'm viewing the login page with an error message