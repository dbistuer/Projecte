Feature: Delete cinema
  In order to delete a cinema
  as an employee
  I want to delete it from the database

  Background: There's at least a cinema
    Given The staff has registered
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs into the account
      |   username       |   password        |
      |   employee       |   1234            |
    Given the following cinema
      | adress   |   name    |   description |
      | a        |   a       |   a           |

  Scenario: Look up the current cinemas
    When We enter the list of cinemas

    Then I press delete
