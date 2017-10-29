from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    app.group.edit_first_group(Group(name="group1(ed)", header="header1(ed)", footer="footer1(ed)"))

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    app.group.edit_first_group(Group(name="New group"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    app.group.edit_first_group(Group(header="New header"))
