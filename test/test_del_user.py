from model.myuser import MyUser


def test_del_user(app):
    app.user.delete_first_user()
