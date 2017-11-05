# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Oleg(ed)", lastname="Wesovoy", nickname="olegles", company="Google",
          address="Belgorod, Lenina str., 12", mobile_phone="8-052-706-15-22", email="oleg.lesovoy@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Vasilyeva", nickname="lenchik", company="mailRu",
            address="Belgorod, Lenina str., 82", mobile_phone="8-105-068-27-66", email="lena.vasya@gmail.com")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

