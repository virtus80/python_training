# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Vasyly", lastname="Petrov", nickname="vasya26", company="Google",
                               address="Belgorod, Lenina str., 10", mobile_phone="8-052-709-16-22", email="vasya.petrov@gmail.com"))
    app.session.logout()


