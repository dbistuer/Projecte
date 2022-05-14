Feature: View cinemas
  In order to see the cinemas
  as an employee
  I want to view a list of cinemas

  Background: There's at least a cinema
    Given The staff has logged in
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs in the account
      |   username       |   password        |
      |   employee        |   1234            |
    Given Exists the following cinema
      | adress    |   name    | description  |
      | a         |   a       |   a          |

  Scenario: Look up the current cinemas
    When I visit the list of cinemas

    Then I look up the cinema
      | adress    |   name    | description  |
      | a         |   a       |   a          |
