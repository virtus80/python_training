# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string_for_names(prefix, maxlen):
    symbols = string.ascii_letters + "'" + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phones(maxlen):
    symbols = string.digits*3 + " +()" + "-"*3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_address(maxlen):
    symbols = string.ascii_letters + string.digits + " ,."*5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_email(maxlen):
    symbols = string.ascii_letters*3 + string.digits + "-_#&+"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string_for_names("name", 15), lastname=random_string_for_names("surname", 20),
            nickname=random_string_for_address(20), company=random_string_for_names("company", 30),
            address=random_string_for_address(60), homephone=random_string_for_phones(14),
            workphone=random_string_for_phones(14), mobilephone=random_string_for_phones(14),
            secondaryphone=random_string_for_phones(14),email=random_string_for_email(30) + "@" + random.choice(["mail.ru", "gmail.com",
            "yandex.ru", "i.ua", "ukr.net"])) for i in range(3)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



