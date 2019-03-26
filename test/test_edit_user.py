from model.myuser import MyUser


def test_edit_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                           "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                           "Berdsk", "1", "142"))
    app.user.edit_first_user(MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                           "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                           "Berdsk", "1", "143"))
    app.session.logout()