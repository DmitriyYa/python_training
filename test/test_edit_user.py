from model.myuser import MyUser


def test_edit_first_user_all(app):
    app.user.edit_first_user(
        MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
               "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
               "Berdsk", "1", "143"))


def test_edit_first_user_firstname(app):
    app.user.edit_first_user(
        MyUser(first_name="New name"))


def test_edit_first_user_middlename(app):
    app.user.edit_first_user(
        MyUser(middle_name="New middle name"))


def test_edit_first_user_bday(app):
    app.user.edit_first_user(
        MyUser(b_day="12"))


def test_edit_first_user_amonth(app):
    app.user.edit_first_user(
        MyUser(a_month="April"))
