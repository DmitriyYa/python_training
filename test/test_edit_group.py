from model.group import Group
from random import randrange

def test_edit_some_group_all(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))

    group = Group(name="NewName", header="NewHeder", footer="NewFooter")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)

    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="New name"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="NewHeder"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(footer="NewFooter"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#