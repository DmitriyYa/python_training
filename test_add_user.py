# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

from myuser import MyUser


class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.create_user(wd, MyUser("Dima", "Miha", "Yakov", "DimYa", "t", "N", "1", "9", "7", "7", "d", "d.ya2@mail.ru",
                                  "d.ya3@mail.ru", "www.dima.ru", "15", "April", "1983", "1", "January", "1970",
                                  "Berdsk", "1", "142"))
        self.logout(wd)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_user(self, wd, my_user):
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

    def open_group_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        wd.find_element_by_name("user").send_keys("ADMIN")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
