from model.myuser import MyUser
import random


def test_edit_first_user_all(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(MyUser(first_name="user"))

    old_users = db.get_user_list()
    user_random = random.choice(old_users)

    user = MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                  "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                  "Berdsk", "1", "142")
    user.id = user_random.id
    app.user.edit_user_by_id(user, user.id)

    new_users = db.get_user_list()
    assert len(old_users) == len(new_users)

    old_users.remove(user_random)
    old_users.append(user)
    assert sorted(old_users, key=MyUser.id_or_max) == sorted(new_users, key=MyUser.id_or_max)

    if check_ui:
        assert sorted(new_users, key=MyUser.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                                 key=MyUser.id_or_max)

# def test_edit_first_user_firstname(app):
#     if app.user.count() == 0:
#         app.user.create(MyUser(first_name="user"))
#     old_users = app.user.get_user_list()
#     app.user.edit_first_user(
#         MyUser(first_name="New name"))
#     new_users = app.user.get_user_list()
#     assert len(old_users) == len(new_users)
#
#
# def test_edit_first_user_middlename(app):
#     if app.user.count()==0:
#         app.user.create(MyUser(first_name="user"))
#     old_users = app.user.get_user_list()
#     app.user.edit_first_user(
#         MyUser(middle_name="New middle name"))
#     new_users = app.user.get_user_list()
#     assert len(old_users) == len(new_users)
#
#
# def test_edit_first_user_bday(app):
#     if app.user.count()==0:
#         app.user.create(MyUser(first_name="user"))
#     old_users = app.user.get_user_list()
#     app.user.edit_first_user(
#         MyUser(b_day="12"))
#     new_users = app.user.get_user_list()
#     assert len(old_users) == len(new_users)
#
#
# def test_edit_first_user_amonth(app):
#     if app.user.count()==0:
#         app.user.create(MyUser(first_name="user"))
#     old_users = app.user.get_user_list()
#     app.user.edit_first_user(
#         MyUser(a_month="April"))
#     new_users = app.user.get_user_list()
#     assert len(old_users) == len(new_users)
