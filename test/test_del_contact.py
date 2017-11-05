from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Alexey", lastname="Zhdanov", nickname="lyoha", company="Yandex",
            address="Belgorod, Lenina str., 8", mobile_phone="8-241-326-45-26", email="lyoha48@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts