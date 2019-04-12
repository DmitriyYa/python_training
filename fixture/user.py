from time import sleep
from selenium.webdriver.support.ui import Select
from model.myuser import MyUser


class UserHelper:
    user_cache = None

    def __init__(self, app):
        self.app = app

    def return_to_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, my_user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form_user(my_user)
        wd.find_element_by_name("submit").click()
        self.return_to_user_page()
        self.user_cache = None

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.open_user_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        # Todo
        sleep(2)
        self.user_cache = None

    def open_user_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, feild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(feild_name).clear()
            wd.find_element_by_name(feild_name).send_keys(text)

    def change_field_value_select_by_visible_text(self, feild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(feild_name).click()
            Select(wd.find_element_by_name(feild_name)).select_by_visible_text(text)

    def select_user_by_index(self, index):
        wd = self.app.wd
        list = []
        for el in wd.find_elements_by_tag_name("img"):
            if "Edit" == el.get_attribute("title"):
                list.append(el)
        list[index].click()

    def edit_first_user(self):
        self.delete_user_by_index(0)

    def edit_user_by_index(self, my_user, index):
        wd = self.app.wd
        self.open_user_page()
        self.select_user_by_index(index)
        self.fill_form_user(my_user)
        wd.find_element_by_name("update").click()
        self.return_to_user_page()
        self.user_cache = None

    def fill_form_user(self, my_user):
        wd = self.app.wd
        self.change_field_value("firstname", my_user.first_name)
        self.change_field_value("middlename", my_user.middle_name)
        self.change_field_value("lastname", my_user.last_name)
        self.change_field_value("nickname", my_user.nick_name)
        self.change_field_value("title", my_user.title)
        self.change_field_value("company", my_user.company)
        self.change_field_value("home", my_user.home)
        self.change_field_value("mobile", my_user.mobile)
        self.change_field_value("work", my_user.work)
        self.change_field_value("fax", my_user.fax)
        self.change_field_value("email", my_user.email)
        self.change_field_value("email2", my_user.email2)
        self.change_field_value("email3", my_user.email3)
        self.change_field_value("homepage", my_user.homepage)
        self.change_field_value_select_by_visible_text("bday", my_user.b_day)
        self.change_field_value_select_by_visible_text("bmonth", my_user.b_month)
        self.change_field_value("byear", my_user.b_year)
        self.change_field_value_select_by_visible_text("aday", my_user.a_day)
        self.change_field_value_select_by_visible_text("amonth", my_user.a_month)
        self.change_field_value("ayear", my_user.a_year)
        self.change_field_value("address2", my_user.address2)
        self.change_field_value("phone2", my_user.phone2)
        self.change_field_value("notes", my_user.notes)

    def count(self):
        wd = self.app.wd
        self.open_user_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_user_page()
            self.user_cache = []
            if self.count() > 0:
                for entry in wd.find_element_by_id("maintable").find_elements_by_name("entry"):
                    td = entry.find_elements_by_tag_name("td")
                    user_id = td[0].find_element_by_name("selected[]").get_attribute("value")
                    first_name = td[2].text
                    last_name = td[1].text
                    self.user_cache.append(MyUser(first_name=first_name, last_name=last_name, id=user_id))
        return self.user_cache
