import re
from random import randrange


def test_phones_on_homepage(app):
    user_list_from_home_page = app.user.get_user_list_from_home_page()
    index = randrange(len(user_list_from_home_page))

    some_user_from_home_page = user_list_from_home_page[index]

    some_user_from_edit_page = app.user.get_user_info_by_index_from_edit_page(index)

    assert some_user_from_home_page.first_name == clear_names(some_user_from_edit_page.first_name)

    assert some_user_from_home_page.last_name == clear_names(some_user_from_edit_page.last_name)

    assert some_user_from_home_page.all_phones_from_home_page == merg_phones_like_on_home_page(
        some_user_from_edit_page)

    assert some_user_from_home_page.all_emails_from_home_page == merg_emails_like_on_home_page(some_user_from_edit_page)

    assert some_user_from_home_page.address == some_user_from_edit_page.address


# def test_phones_on_view_page(app):
#     user_list_from_home_page = app.user.get_user_list_from_home_page()
#     index = randrange(len(user_list_from_home_page))
#
#     user_from_view_page = app.user.get_user_info_by_index_from_view_page(index)
#     user_from_edit_page = app.user.get_user_info_by_index_from_edit_page(index)
#     assert user_from_view_page.home_phone == user_from_edit_page.home_phone
#     assert user_from_view_page.work_phone == user_from_edit_page.work_phone
#     assert user_from_view_page.mobile_phone == user_from_edit_page.mobile_phone
#     assert user_from_view_page.phone2 == user_from_edit_page.phone2


def clear(st):
    return re.sub("[() -]", "", st)


def clear_email(st):
    return re.sub("[()]", "", st)


def clear_names(st):
    if st and st[-1]== " ":
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
