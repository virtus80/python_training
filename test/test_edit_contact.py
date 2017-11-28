# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Oleg(ed)", lastname="Wesovoy", nickname="olegles", company="Google",
                                   address="Belgorod, Lenina str., 12", mobilephone="8-052-706-15-22", email="oleg.lesovoy@gmail.com"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Vasilyeva", nickname="lenchik", company="mailRu",
                      address="Belgorod, Lenina str., 82", mobilephone="8-105-068-27-66", email="lena.vasya@gmail.com")
    contact_for_edit = random.choice(old_contacts)
    index = old_contacts.index(contact_for_edit)
    app.contact.edit_contact_by_id(contact_for_edit.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = Contact(id=contact_for_edit.id, firstname=contact.firstname, lastname=contact.lastname, nickname=contact.nickname,
                    company=contact.company, address=contact.address, homephone=contact.homephone, workphone=contact.workphone,
                    mobilephone=contact.mobilephone, secondaryphone=contact.secondaryphone, email=contact.email, email2=contact.email2, email3=contact.email3)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        db_list = map(db.clean_contact, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

