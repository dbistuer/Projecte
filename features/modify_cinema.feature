Feature: Modify cinema
  In order to modify a cinema
  as an employee
  I want to modify the description

  Background: There's at least a cinema
    Given The user has logged
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs
      |   username       |   password        |
      |   employee        |   1234            |
    Given the following cinema
      | adress   |   name    |   description |
      | a        |   a       |   a           |

  Scenario: Look up a current cinema
    When We enter the details of a cinema

    Then I modify the details of a cinema from the database
    |   description |
    |   b           |
