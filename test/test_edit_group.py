from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="group1(ed)", header="header1(ed)", footer="footer1(ed)"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
