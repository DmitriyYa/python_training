from model.myuser import MyUser


def test_del_user(app):
    app.session.login(username="admin", password="secret")
    app.user.delete_first_user()
    app.session.logout()
