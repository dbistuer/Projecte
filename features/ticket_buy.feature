# Created by opolo at 10/05/2022
Feature: Ticket buys
  In order to buy a room movie on a cinema
  as an client
  I want to view a list of films

  Background: There's at least moive_cinema_room in a database
    Given The staff has an account
      | name        |   DNI         |   address     |   phoneNumber     |   email           |   alias       |   password        |   cardNumber                  |
      | Adri        |   22450225V   |   Carrer      |   642897512       |   ma@hotmail.com   |   employee        |   1234            |   ES9121000418450200051332    |
    Then The staff is logged in the account
      |   username       |   password        |
      |   employee        |   1234            |
    Given Exists the following room_cinema_movie
      | adress        |   name          |   number      |   capacity     | mov_name | gender | duration | synopsis     | classification|   date_movie     |
      | Calles        |   Nombre        |   14          |   100          | dr.strange| action| 120      | Va de un mago| 18            |   2022-05-10     |





  Scenario: Look up the current movie_cinema_room
    When I visit the movie list

    Then I select how many tickets i want

