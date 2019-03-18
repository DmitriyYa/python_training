# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_user(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_group_page(driver)
        self.create_user(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_user(self, driver):
        driver.find_element_by_name("firstname").send_keys("Dima")
        driver.find_element_by_name("middlename").send_keys("Miha")
        driver.find_element_by_name("lastname").send_keys("Yakov")
        driver.find_element_by_name("nickname").send_keys("DimYa")
        driver.find_element_by_name("title").send_keys("t")
        driver.find_element_by_name("company").send_keys("N")
        driver.find_element_by_name("home").send_keys("1")
        driver.find_element_by_name("mobile").send_keys("9")
        driver.find_element_by_name("work").send_keys("7")
        driver.find_element_by_name("fax").send_keys("7")
        driver.find_element_by_name("email").send_keys("d")
        driver.find_element_by_name("email2").send_keys("d.ya2@mail.ru")
        driver.find_element_by_name("email3").send_keys("d.ya3@mail.ru")
        driver.find_element_by_name("homepage").send_keys("www.dima.ru")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("15")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[17]").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("April")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[38]").click()
        driver.find_element_by_name("byear").send_keys("1983")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[3]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("January")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[35]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1970")
        driver.find_element_by_name("address2").send_keys("Berdsk")
        driver.find_element_by_name("phone2").send_keys("1")
        driver.find_element_by_name("notes").send_keys("142")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def open_group_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver):
        driver.find_element_by_name("user").send_keys("ADMIN")
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_id("LoginForm").submit()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/edit.php")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
