from selenium.webdriver.support.ui import Select

class UserHelper:

    def __init__(self, app):
        self.app=app

    def create(self, my_user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(my_user.first_name)
        wd.find_element_by_name("middlename").send_keys(my_user.middle_name)
        wd.find_element_by_name("lastname").send_keys(my_user.last_name)
        wd.find_element_by_name("nickname").send_keys(my_user.nick_name)
        wd.find_element_by_name("title").send_keys(my_user.title)
        wd.find_element_by_name("company").send_keys(my_user.company)
        wd.find_element_by_name("home").send_keys(my_user.home)
        wd.find_element_by_name("mobile").send_keys(my_user.mobile)
        wd.find_element_by_name("work").send_keys(my_user.work)
        wd.find_element_by_name("fax").send_keys(my_user.fax)
        wd.find_element_by_name("email").send_keys(my_user.email)
        wd.find_element_by_name("email2").send_keys(my_user.email2)
        wd.find_element_by_name("email3").send_keys(my_user.email3)
        wd.find_element_by_name("homepage").send_keys(my_user.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(my_user.b_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(my_user.b_month)
        wd.find_element_by_name("byear").send_keys(my_user.b_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(my_user.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(my_user.a_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(my_user.a_year)
        wd.find_element_by_name("address2").send_keys(my_user.address2)
        wd.find_element_by_name("phone2").send_keys(my_user.phone2)
        wd.find_element_by_name("notes").send_keys(my_user.notes)
        wd.find_element_by_name("submit").click()