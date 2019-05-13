from model.group import Group
import random

def test_edit_some_group_all(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)

    group = Group(name="NewName", header="NewHeder", footer="NewFooter")
    group.id = group_random.id
    app.group.edit_group_by_id(group, group.id)

    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

    old_groups.remove(group_random)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert  sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list_in_group_page(), key=Group.id_or_max)