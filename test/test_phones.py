import re
from model.myuser import MyUser


def test_user_contacts_on_homepage(app, db):
    user_list_from_home_page = sorted(app.user.get_user_list_from_home_page(), key=MyUser.id_or_max)

    user_list_from_db = sorted(db.get_user_list(), key=MyUser.id_or_max)

    for i in range(len(user_list_from_home_page)):
        assert user_list_from_home_page[i].first_name == clear_names(user_list_from_db[i].first_name)
        assert user_list_from_home_page[i].last_name == clear_names(user_list_from_db[i].last_name)
        assert user_list_from_home_page[i].address == user_list_from_db[i].address
        assert user_list_from_home_page[i].all_emails_from_home_page == merg_emails_like_on_home_page(
            user_list_from_db[i])
        assert user_list_from_home_page[i].all_phones_from_home_page == merg_phones_like_on_home_page(
            user_list_from_db[i])


def clear_address(st):
    if st == "":
        return None


def clear(st):
    return re.sub("[() -]", "", st)


def clear_email(st):
    return re.sub("[()]", "", st)


def clear_names(st):
    if st and st[-1] == " ":
        return st[0:-1]
    else:
        return st


def merg_phones_like_on_home_page(user):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [user.home_phone, user.mobile_phone, user.work_phone,
                           user.phone2]))))


def merg_emails_like_on_home_page(user):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear_email(x),
                   filter(lambda x: x is not None,
                          [user.email, user.email2, user.email3]))))
