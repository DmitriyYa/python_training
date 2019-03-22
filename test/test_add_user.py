# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.myuser import MyUser


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.create_user(MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                           "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                           "Berdsk", "1", "142"))
    app.session.logout()
