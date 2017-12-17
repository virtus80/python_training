Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name    | header     | footer     |
  | namebdd1| headerbdd1 | footerbdd1 |
  | namebdd2| headerbdd2 | footerbdd2 |