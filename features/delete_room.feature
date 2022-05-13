Feature: Delete room
  In order to delete a rooms of a cinema
  as an employee
  I want to delete it from the database

  Background: There's at least room in a cinema
    Given The staff has registered
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs into the account
      |   username       |   password        |
      |   employee        |   1234            |
    Given Given the following room in a cinema
      | adress                |   name          |   number      |   capacity     |
      | Calle la palma        |   Cinemax       |   3           |   300          |

  Scenario: Look up the current cinemas
    When We enter the cinema list

    Then I look up the details of a room of a cinema
