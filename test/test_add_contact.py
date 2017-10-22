# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Oleg", lastname="Lesovoy", nickname="olegles", company="Google",
                               address="Belgorod, Lenina str., 12", mobile_phone="8-052-706-15-22", email="oleg.lesovoy@gmail.com"))
    app.session.logout()


