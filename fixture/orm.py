# -*- coding: utf-8 -*-
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.myuser import MyUser
from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        users = Set(lambda: ORMFixture.ORMUser, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMUser(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='users',
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)  # privazka k bd
        self.db.generate_mapping()  # preobrazovanie dannih iz tablic v obecti

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_users_to_model(self, users):
        def convert(user):
            return MyUser(id=str(user.id), first_name=user.firstname, last_name=user.lastname, address=user.address, home_phone=user.home_phone, mobile_phone=user.mobile_phone, work_phone=user.work_phone,
                          phone2=user.phone2, email=user.email, email2=user.email2, email3=user.email3)

        return list(map(convert, users))

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(u for u in ORMFixture.ORMUser if u.deprecated is None))

    @db_session
    def get_users_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(orm_group.users)

    @db_session
    def get_users_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(
            select(u for u in ORMFixture.ORMUser if u.deprecated is None and orm_group not in u.groups))