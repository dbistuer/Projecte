Feature: View rooms
  In order to see the rooms of a cinema
  as an employee
  I want to view a list of rooms

  Background: There's at least room in a cinema
    Given The staff has logged in
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs in the account
      |   username       |   password        |
      |   employee        |   1234            |
    Given Exists the following room in a cinema
      | adress                |   name          |   number      |   capacity     |
      | Roca llaurador        |   Llauren       |   10          |   230          |

  Scenario: Look up the current cinemas
    When I visit the cinema list

    Then I look up the rooms in the cinema
      |   number     |   capacity        |
      |   10         |   230             |