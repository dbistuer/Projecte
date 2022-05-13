Feature: Modify room
  In order to modify a rooms of a cinema
  as an employee
  I want to modify the capacity

  Background: There's at least room in a cinema
    Given The user has logged
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs
      |   username       |   password        |
      |   employee        |   1234            |
    Given Given the following room of a cinema
      | adress       |   name          |   number      |   capacity     |
      | Xanxi        |   Cinema persa  |   7           |   225          |

  Scenario: Look up a current room of a cinema
    When We enter the details of a room

    Then I modify the details of a room from the database
    | capacity |
    | 100      |
