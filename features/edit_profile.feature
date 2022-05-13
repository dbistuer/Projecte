Feature: Edit profile/client
  In order to edit my user profile
  As a logged user
  I want to edit my profile

  Background: There is a registered user 
    Given Exists the following user
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   marc        |   1234            |   ES9121000418450200051332    |
  
  Scenario: Edit succesfully a profile
    When I visit the profile page
    Then I login as user "marc"
    |   username       |   password        | 
    |   marc        |   1234            |
    Then I click the edit profile button in order to go to the edit profile page
    Then I edit my profile with this new data
        | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias      |   cardNumber                  |
        | Maria        |   78101066N   |   Carrer Paraguay      |   630897511       |   maria@hotmail.com   |   maria       |   ES9121000418450200051332    |
    And The user "marc" has been modified with the previous new data
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias      |   cardNumber                  |
        | Maria        |   78101066N   |   Carrer Paraguay      |   630897511       |   maria@hotmail.com   |   maria       |   ES9121000418450200051332    | 

  Scenario: Edit unsuccesfully a profile
    When I visit the profile page
    Then I login as user "marc"
    |   username       |   password        | 
    |   marc        |   1234            |
    Then I click the edit profile button in order to go to the edit profile page
    Then I edit my profile with this new data
        | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias      |   cardNumber  |
        | Maria        |   1   |   Carrer Paraguay      |   1       |   maria@hotmail.com   |   maria       |   1    |
    And I can see an error 
