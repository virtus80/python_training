# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Oleg(ed)", lastname="Wesovoy", nickname="olegles", company="Google",
          address="Belgorod, Lenina str., 12", mobile_phone="8-052-706-15-22", email="oleg.lesovoy@gmail.com"))
    app.contact.edit_first_contact(Contact(firstname="Elena", lastname="Vasilyeva", nickname="lenchik", company="mailRu",
            address="Belgorod, Lenina str., 82", mobile_phone="8-105-068-27-66", email="lena.vasya@gmail.com"))

