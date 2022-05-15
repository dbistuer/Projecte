# Created by dbist at 14/05/2022
# Created by dbist at 14/05/2022
Feature: Edit an existing movie
  In order to verify the can edit a movie throug th page
  as staff
  I want edit a movie

  Background: I have the user
    Given create user staff
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | employee    |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com  |   employee    |   1234            |   ES9121000418450200051332    |
    When The staff logs in
      |   username       |   password        |
      |   employee        |   1234            |
    Then Create a movie on database and go to edit page


  Scenario: We try to modify one movie
    Given those data fulfill on form
    | name     | duration   | synopsis     | gender  | classification  | image                     |
    | Changed  | 245         | movie changed| Action | X               | \features\image\test2.jpg |
