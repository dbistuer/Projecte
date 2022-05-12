Feature: View rooms
  In order to see the rooms of a cinema
  as an employee
  I want to view a list of rooms

  Background: There's at least room in a cinema
    Given Exists the following room in a cinema
      | adress               |   name         |   number     |   capacity     | cinema |
      | Roca labrador        |   Lauren       |   1          |   100          | 1      |

  Scenario: Look up the current cinemas
    When I visit the cinema list

    Then I look up the rooms in the cinema
      |   number    |   capacity        |
      |   1         |   100             |