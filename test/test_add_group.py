# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("group1", "groupheder1", "groupfooter1"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
