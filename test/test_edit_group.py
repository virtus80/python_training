from model.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    old_groups = app.group.get_group_list()
    group = Group(name="group1(ed)", header="header1(ed)", footer="footer1(ed)")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    index = randrange(len(old_groups))
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group before editing", header="header edited group", footer="footer edited group"))
    old_groups = app.group.get_group_list()
    group = Group(header="New header")
    group.id = old_groups[0].id
    index = randrange(len(old_groups))
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''