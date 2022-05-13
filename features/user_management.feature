Feature: User management 
  In order to manage user roles or delete users
  As an admin user
  I want to change roles or delete users

    Background: There is a registered normal user, a registered employee user and an admin user 
    Given Exists the following users
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Marc        |   78101067J   |   Carrer      |   642897511       |   m@hotmail.com   |   normal_user        |   1234            |   ES9121000418450200051332    |
      | Juan        |   78101066N   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
      | Bob         |   78101067J   |   Carrer      |   642897513       |   mas@hotmail.com   |   admin        |   1234            |   ES9121000418450200051332    |

    Scenario: Visit the user management page as a normal_user
    When I visit the user management page
    Then I login as user "normal_user"
    |   username    |   password        | 
    |   normal_user        |   1234            |
    And I see that this account does not have access to this page
    
    Scenario: Visit the user management page as an employee
    When I visit the user management page
    Then I login as user "employee"
    |   username    |   password        | 
    |   employee        |   1234            |
    And I see that this account does not have access to this page

    Scenario: Change roles of users
    When I visit the user management page
    Then I login as user "admin"
    |   username    |   password        | 
    |   admin        |   1234            |
    Then I change the role of the user "employee" to admin
    Then The user "employee" has admin permissions
    Then I change the role of the user "employee" to normal_user
    Then The user "employee" has normal user permissions
    Then I change the role of the user "employee" to employee
    Then The user "employee" has employee permissions
    Then I change the role of the user "normal_client" to admin
    And the user "normal_client has admin permissions
    Scenario: Delete users
    When I visit the user management page
    Then I login as user "admin"
    |   username    |   password        | 
    |   admin        |   1234            |
    Then I delete the user "employee"
    Then The user "employee" is not in the database
    Then I delete the user "normal_user"
    And The user "normal_user" is not in the database
