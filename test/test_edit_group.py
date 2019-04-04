from model.group import Group


def test_edit_first_group_all(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group("NewName", "NewHeder", "NewFooter"))
    app.session.logout()


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New name"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="NewHeder"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="NewFooter"))
    app.session.logout()
