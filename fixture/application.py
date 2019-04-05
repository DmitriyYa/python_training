from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.open_home_page()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

