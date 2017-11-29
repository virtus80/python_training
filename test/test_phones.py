from random import randrange
from model.contact import Contact
import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def test_contact_attributes_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == clear_address_like_on_homepage(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

def test_contact_attributes_on_home_page_with_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert list(map(lambda x: x.firstname, contacts_from_home_page)) == list(map(lambda x: x.firstname.strip(), contacts_from_db))
    assert list(map(lambda x: x.lastname, contacts_from_home_page)) == list(map(lambda x: x.lastname.strip(), contacts_from_db))
    assert list(map(lambda x: x.address, contacts_from_home_page)) == list(map(lambda x: x.address.strip(), contacts_from_db))
    assert list(map(lambda x: x.all_emails_from_homepage, contacts_from_home_page)) == list(map(merge_emails_like_on_homepage, contacts_from_db))
    assert list(map(lambda x: x.all_phones_from_homepage.replace("\n\n", "\n"), contacts_from_home_page)) == list(map(merge_phones_like_on_homepage, contacts_from_db))


def clear_phones_like_on_homepage(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phones_like_on_homepage(x), filter(lambda x: x is not None,
                                                                                   [contact.homephone,
                                                                                    contact.mobilephone,
                                                                                    contact.workphone,
                                                                                    contact.secondaryphone]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                          [contact.email, contact.email2, contact.email3])))

def clear_address_like_on_homepage(s):
    if s is not None:
        address_line = s.split("\n")
        line_without_spaces = []
        for line in address_line:
            line_without_spaces.append(line.strip())
        formatted_address = "\n".join(line_without_spaces)
        return formatted_address
