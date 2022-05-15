# Created by dbist at 14/05/2022
Feature: Delete an existing movie
  In order to verify the can delete a movie throug the page
  as staff
  I want edit a movie

  Background: I have the user
    Given create user staff
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | employee    |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com  |   employee    |   1234            |   ES9121000418450200051332    |
    When The staff logs in
      |   username       |   password        |
      |   employee        |   1234            |
    Then Create a movie on database and go to detail page


  Scenario: We try to delete one movie
    Given push delete and verify that has been deleted