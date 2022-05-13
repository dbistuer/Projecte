Feature: Delete the account
  In order to delete the account
  As a logged user
  I want to delete the account from the database

   Background: There is a registered user 
    Given Exists the following user
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   marc        |   1234            |   ES9121000418450200051332    |

       
   Scenario: Delete succesfully an account
    When I visit the delete account page
    Then I login as user "marc"
    |   username    |   password        | 
    |   marc        |   1234            |
    Then I click the confirmation button in order to delete the account
    And The user "marc" has been deleted, it does not exist in the database
