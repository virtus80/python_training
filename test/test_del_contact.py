from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Alexey", lastname="Zhdanov", nickname="lyoha", company="Yandex",
                                   address="Belgorod, Lenina str., 8", mobilephone="8-241-326-45-26", email="lyoha48@gmail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        db_list = map(db.clean_contact, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)