from model.myuser import MyUser


def test_edit_first_user_all(app):
    if app.user.count() == 0:
        app.user.create(MyUser(first_name="user"))
    old_users = app.user.get_user_list()
    app.user.edit_first_user(
        MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
               "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
               "Berdsk", "1", "143"))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)


def test_edit_first_user_firstname(app):
    if app.user.count() == 0:
        app.user.create(MyUser(first_name="user"))
    old_users = app.user.get_user_list()
    app.user.edit_first_user(
        MyUser(first_name="New name"))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)


def test_edit_first_user_middlename(app):
    if app.user.count()==0:
        app.user.create(MyUser(first_name="user"))
    old_users = app.user.get_user_list()
    app.user.edit_first_user(
        MyUser(middle_name="New middle name"))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)


def test_edit_first_user_bday(app):
    if app.user.count()==0:
        app.user.create(MyUser(first_name="user"))
    old_users = app.user.get_user_list()
    app.user.edit_first_user(
        MyUser(b_day="12"))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)


def test_edit_first_user_amonth(app):
    if app.user.count()==0:
        app.user.create(MyUser(first_name="user"))
    old_users = app.user.get_user_list()
    app.user.edit_first_user(
        MyUser(a_month="April"))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
