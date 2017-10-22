# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(firstname="Vasyly", lastname="Petrov", nickname="vasya26", company="Google",
        address="Belgorod, Lenina str., 10", mobile_phone="8-052-709-16-22", email="vasya.petrov@gmail.com"))
    app.logout()


