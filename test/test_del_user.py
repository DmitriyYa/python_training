from model.myuser import MyUser


def test_del_user(app):
    if app.user.count()==0:
        app.user.create(MyUser(first_name="user"))
    app.user.delete_first_user()
