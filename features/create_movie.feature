# Created by dbist at 14/05/2022
Feature: Create movie
  In order to create a movie
  as employee
  I want to be able to fulfill a form

    Background: I have the movie data
    Given The user has logged in
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | employee    |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com  |   employee    |   1234            |   ES9121000418450200051332    |
    When The staff logs in
      |   username       |   password        |
      |   employee        |   1234            |
    Then We look into the add movie

  Scenario: We try to create a movie
   When We look into the navbar and apears the menu item "Add movie" click on it

    Then We fulfill the form and create the movie
      | name      | duration    | synopsis        | gender  | classification | image                    |
      | Avengers  | 125         | movie of marvel | War     | 7              | \features\image\test.png |
