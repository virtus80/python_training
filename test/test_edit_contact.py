# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Oleg(ed)", lastname="Wesovoy", nickname="olegles", company="Google",
          address="Belgorod, Lenina str., 12", mobile_phone="8-052-706-15-22", email="oleg.lesovoy@gmail.com"))

