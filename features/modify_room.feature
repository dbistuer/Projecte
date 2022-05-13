Feature: Modify room
  In order to modify a rooms of a cinema
  as an employee
  I want to modify the capacity

  Background: There's at least room in a cinema
    Given Given the following room of a cinema
      | adress       |   name          |   number      |   capacity     |
      | Xanxi        |   Cinema persa  |   7           |   225          |

  Scenario: Look up a current room of a cinema
    When We enter the details of a room

    Then I modify the details of a room from the database
    | capacity |
    | 100      |
