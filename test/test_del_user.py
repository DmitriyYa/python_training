from model.myuser import MyUser


def test_del_user(app):
    if app.user.count() == 0:
        app.user.create(MyUser(first_name="user"))
    old_users = app.user.get_user_list()
    app.user.delete_first_user()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)

    old_users[0:1] = []
    assert old_users == new_users
