# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Vasyly", lastname="Smirnov", nickname="smirny", company="Google",
                               address="Belgorod, Lenina str., 10", mobile_phone="8-051-750-45-26", email="vas.smirnov@gmail.com"))
    app.session.logout()


