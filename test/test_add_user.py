# -*- coding: utf-8 -*-
from model.myuser import MyUser


def test_add_user(app):
    user = MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                  "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                  "Berdsk", "1", "142")
    old_users = app.user.get_user_list()
    app.user.create(user)

    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list()

    old_users.append(user)
    assert sorted(old_users, key=MyUser.id_or_max) == sorted(new_users, key=MyUser.id_or_max)