# Created by opolo at 10/05/2022
Feature: Ticket buys
  In order to buy a roomovie on a cinema
  as an client
  I want to view a list of films

  Background: There's at least moive_cinema_room in a database
    Given Exists the following room_cinema_movie
      | Cinema               |   Movie         |   Room     |   date_movie     |
      | 1                    |   1             |   1        |   2022-05-10     |

  Scenario: Look up the current movie_cinema_room
    When I visit the movie list

    Then I select how many tickets i want

    Then I confirm the ticket is bought
      |   price    |
      |   8.5      |