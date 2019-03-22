from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.heder)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.open_group_page()

    def create_user(self, my_user):
        wd = self.wd
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

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
