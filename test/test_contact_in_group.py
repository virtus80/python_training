# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


conn = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(
            Group(name="group before deleting", header="header deleted group", footer="footer deleted group"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = conn.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="Alexey", lastname="Zhdanov", nickname="lyoha", company="Yandex",
                                   address="Belgorod, Lenina str., 8", mobilephone="8-241-326-45-26", email="lyoha48@gmail.com"))
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact, group)
    assert contact in conn.get_contacts_in_group(group)

def test_remove_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(
            Group(name="group before deleting", header="header deleted group", footer="footer deleted group"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Alexey", lastname="Zhdanov", nickname="lyoha", company="Yandex",
                                   address="Belgorod, Lenina str., 8", mobilephone="8-241-326-45-26", email="lyoha48@gmail.com"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = conn.get_contacts_in_group(group)
    if len(contacts) == 0:
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
        contacts = conn.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.remove_contact_from_group(contact, group)
    assert contact in conn.get_contacts_not_in_group(group)
    