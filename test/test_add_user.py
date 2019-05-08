# -*- coding: utf-8 -*-
from model.myuser import MyUser


def test_add_user(app, db, json_users, check_ui):
    user = json_users
    old_users = db.get_user_list()
    app.user.create(user)

    new_users = db.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=MyUser.id_or_max) == sorted(new_users, key=MyUser.id_or_max)

    if check_ui:
        assert sorted(new_users, key=MyUser.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                                 key=MyUser.id_or_max)
