from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="group1(ed)", header="header1(ed)", footer="footer1(ed)"))

def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="New group"))

def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="New header"))
