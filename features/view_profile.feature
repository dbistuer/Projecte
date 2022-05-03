Feature: View profile
  In order check my user profile
  As a logged user
  I want view my profile

  Background: There is a registered user 
    Given Exists the following user
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   marc        |   1234            |   ES9121000418450200051332    |

  Scenario: Access succesfully the profile page 
    When I visit the profile page and I login 
    |   username       |   password        | 
    |   marc        |   1234            |
    Then I'm viewing the user details
    | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   cardNumber                  |
    | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   marc        |   ES9121000418450200051332    |