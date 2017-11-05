# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Vasyly", lastname="Smirnov", nickname="smirny", company="Google",
                               address="Belgorod, Lenina str., 10", mobile_phone="8-051-750-45-26", email="vas.smirnov@gmail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) +1 == len(new_contacts)



