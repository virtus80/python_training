from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <lastname>, <address> and <email>')
def new_contact(firstname, lastname, address, email):
    return Contact(firstname=firstname, lastname=lastname, address=address, email=email)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, app, check_ui, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        db_list = map(db.clean_contact, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Alexey", lastname="Zhdanov", nickname="lyoha", company="Yandex",
                                   address="Belgorod, Lenina str., 8", mobilephone="8-241-326-45-26",
                                   email="lyoha48@gmail.com"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        db_list = map(db.clean_contact, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

@when('I edit the contact in the list with the new contact data')
def edit_contact(app, random_contact, new_contact):
    app.contact.edit_contact_by_id(random_contact.id, new_contact)

@then('the new contact list is equal to the old contact list with changed contact which edited')
def verify_contact_edited(db, non_empty_contact_list, random_contact, new_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    index = old_contacts.index(random_contact)
    app.contact.edit_contact_by_id(random_contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = Contact(id=random_contact.id, firstname=new_contact.firstname, lastname=new_contact.lastname,
                                  address=new_contact.address, email=new_contact.email)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        db_list = map(db.clean_contact, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


