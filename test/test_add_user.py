from model.myuser import MyUser
import random
import pytest


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


def test_add_user_in_group(app, db):
    user_random = random.choice(db.get_user_list())
    group_random = random.choice(db.get_group_list())

    old_users_in_group = db.get_users_in_group(group_random)

    if user_random not in old_users_in_group:
        app.user.add_user_by_id_in_group(user_random, group_random)
    else:
        app.user.del_user_by_id_from_group(user_random, group_random)
        old_users_in_group = db.get_users_in_group(group_random)
        app.user.add_user_by_id_in_group(user_random, group_random)

    new_users_in_group = db.get_users_in_group(group_random)

    old_users_in_group.append(user_random)
    assert sorted(old_users_in_group, key=MyUser.id_or_max) == sorted(new_users_in_group, key=MyUser.id_or_max)


def test_del_user_in_group(app, db):
    user_random = random.choice(db.get_user_list())
    group_random = random.choice(db.get_group_list())

    old_users_in_group = db.get_users_in_group(group_random)

    if user_random in old_users_in_group:
        app.user.del_user_by_id_from_group(user_random, group_random)

    else:
        app.user.add_user_by_id_in_group(user_random, group_random)
        old_users_in_group = db.get_users_in_group(group_random)
        app.user.del_user_by_id_from_group(user_random, group_random)

    new_users_in_group = db.get_users_in_group(group_random)
    old_users_in_group.remove(user_random)

    assert sorted(old_users_in_group, key=MyUser.id_or_max) == sorted(new_users_in_group, key=MyUser.id_or_max)