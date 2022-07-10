from model.group import Group


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_group(Group(name="EditName"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="testHeader"))
    app.group.edit_group(Group(header="EditHeader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
