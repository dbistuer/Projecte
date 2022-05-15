Feature: Create cinema
  
  In order to create a cinema
  as an employee
  I want to be able to fulfill a form

  Background: User logged in
    Given The user has logged in
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff logs in
      |   username       |   password        |
      |   employee        |   1234            |

  Scenario: We try to create a cinema
   When We go to cinema list and press new

    Then We fulfill the form and create the cinema
      | name         |   adress       |   description       |
      | a            |   	a            |   a                 |

