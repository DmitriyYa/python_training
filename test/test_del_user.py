from model.myuser import MyUser
import random


def test_del_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(MyUser(first_name="user"))

    old_users = db.get_user_list()

    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)

    new_users = db.get_user_list()
    assert len(old_users) - 1 == len(new_users)

    old_users.remove(user)
    assert old_users == new_users

    if check_ui:
        assert sorted(new_users, key=MyUser.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                                 key=MyUser.id_or_max)
