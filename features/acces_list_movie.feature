# Created by dbist at 14/05/2022
Feature: Acces to list of movies
  In order to verify the movie list page
  as any user
  I want to acces the page throw the browser

  Background: I have the user
    Given create user staff
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | employee    |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com  |   employee    |   1234            |   ES9121000418450200051332    |
    When The staff logs in
      |   username       |   password        |
      |   employee        |   1234            |
    

  Scenario: We try to acces the page
    Then We look into the list of movies page
