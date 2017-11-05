# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vasyly", lastname="Smirnov", nickname="smirny", company="Google",
        address="Belgorod, Lenina str., 10", mobile_phone="8-051-750-45-26", email="vas.smirnov@gmail.com")
    app.contact.create(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



