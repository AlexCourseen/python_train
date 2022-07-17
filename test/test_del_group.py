from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name='test')
    if app.group.count() == 0:
        app.group.create(group)
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    """удаление первого элемента, т.к. индекс 0-включается,а 1-не включается"""
    old_groups[0:1] = []
    assert old_groups == new_groups


