from model.myuser import MyUser
from random import randrange


def test_del_user(app):
    if app.user.count() == 0:
        app.user.create(MyUser(first_name="user"))

    old_users = app.user.get_user_list_from_home_page()

    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)

    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) - 1 == len(new_users)

    old_users[index:index + 1] = []
    assert old_users == new_users
