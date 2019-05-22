from model.myuser import MyUser
import random
import pytest


def test_del_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(MyUser(first_name="user"))

    with pytest.allure.step('Get user list'):
        old_users = db.get_user_list()

    with pytest.allure.step('Choice random user in user list'):
        user = random.choice(old_users)

    with pytest.allure.step('Del user in addressbook'):
        app.user.delete_user_by_id(user.id)

    with pytest.allure.step('Get new user list and assert len old user list '):
        new_users = db.get_user_list()
        assert len(old_users) - 1 == len(new_users)
    with pytest.allure.step('Get new user list and assert len old user list '):
        old_users.remove(user)
        assert old_users == new_users

    if check_ui:
        assert sorted(new_users, key=MyUser.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                                 key=MyUser.id_or_max)
