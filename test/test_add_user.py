# -*- coding: utf-8 -*-
from model.myuser import MyUser
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [MyUser(first_name="", last_name="", home_phone="", address="", email="")] + [
    MyUser(first_name=random_string("first_name", 10), last_name=random_string("last_name", 10),
           home_phone=random_string("home_phone", 10), address=random_string("address", 20),
           email=random_string("email", 20))
    for i in range(5)
]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_users = app.user.get_user_list_from_home_page()
    app.user.create(user)

    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list_from_home_page()

    old_users.append(user)
    assert sorted(old_users, key=MyUser.id_or_max) == sorted(new_users, key=MyUser.id_or_max)
