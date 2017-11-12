# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Oleg(ed)", lastname="Wesovoy", nickname="olegles", company="Google",
                                   address="Belgorod, Lenina str., 12", mobilephone="8-052-706-15-22", email="oleg.lesovoy@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Vasilyeva", nickname="lenchik", company="mailRu",
                      address="Belgorod, Lenina str., 82", mobilephone="8-105-068-27-66", email="lena.vasya@gmail.com")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

