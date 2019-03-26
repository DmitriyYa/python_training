from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group("group1", "groupheder1", "groupfooter1"))
    app.group.edit_first_group(Group("NewName", "NewHeder", "NewFooter"))
    app.session.logout()
