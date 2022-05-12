Feature: Delete room
  In order to delete a rooms of a cinema
  as an employee
  I want to delete it from the database

  Background: There's at least room in a cinema
    Given Given the following room in a cinema
      | adress                |   name          |   number      |   capacity     |
      | Calle la palma        |   Cinemax       |   3           |   300          |

  Scenario: Look up the current cinemas
    When We enter the cinema list

    Then I look up the details of a room of a cinema
