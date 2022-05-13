Feature: Create room
  In order to create a room for a cinema
  as an employee
  I want to be able to fulfill a form

  Background: There's at least a cinema
    Given The user has logged in
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs in
      |   username       |   password        |
      |   employee        |   1234            |
    Given A cinema exists
      | adress               |   name         |
      | Roca labrador        |   Lauren       |

  Scenario: We try to create a room
   When We look into the cinema details and press try to create a button

    Then We fulfill the form and create the room
      | number       |   capacity       |
      | 1            |   100            |

