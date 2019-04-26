# -*- coding: utf-8 -*-
from model.myuser import MyUser


def test_add_user(app, json_users):
    user = json_users
    old_users = app.user.get_user_list_from_home_page()
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()

    new_users = app.user.get_user_list_from_home_page()
    old_users.append(user)
    assert sorted(old_users, key=MyUser.id_or_max) == sorted(new_users, key=MyUser.id_or_max)
