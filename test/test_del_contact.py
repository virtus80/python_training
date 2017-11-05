from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Alexey", lastname="Zhdanov", nickname="lyoha", company="Yandex",
            address="Belgorod, Lenina str., 8", mobile_phone="8-241-326-45-26", email="lyoha48@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)