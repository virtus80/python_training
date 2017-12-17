Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | lastname | address                        | email            |
  | Igor      | Veselov  | Bryansk, Vishnevaya str. 10    | vesely@gmail.com |
  | Andrey    | Krivenko | Tambov, Zelenaya str., 6. ap.3 | krivenko@mail.ru |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact


Scenario Outline: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname>, <address> and <email>
  When I edit the contact in the list with the new contact data
  Then the new contact list is equal to the old contact list with changed contact which edited

  Examples:
  | firstname  | lastname | address                         | email             |
  | Boris      | Srebnov  | Bryansk, Vishnevaya str., 14    | srebnov@gmail.com |