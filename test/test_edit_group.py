from model.group import Group


def test_edit_first_group_all(app):
    app.group.edit_first_group(Group("NewName", "NewHeder", "NewFooter"))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="New name"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="NewHeder"))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="NewFooter"))
