from model.myuser import MyUser
from random import randrange


def test_edit_first_user_all(app):
    if app.user.count() == 0:
        app.user.create(MyUser(first_name="user"))

    old_users = app.user.get_user_list_from_home_page()
    index = randrange(len(old_users))

    user = MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                  "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                  "Berdsk", "1", "142")
    user.id = old_users[index].id
    app.user.edit_user_by_index(user, index)

    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) == len(new_users)

    old_users[index] = user
    assert sorted(old_users, key=MyUser.id_or_max) == sorted(new_users, key=MyUser.id_or_max)

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
