from model.group import Group


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="EditName")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="testHeader"))
    app.group.edit_group(Group(header="EditHeader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
