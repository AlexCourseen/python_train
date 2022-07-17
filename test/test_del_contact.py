from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstName='testIvan')
    if app.contact.count_contacts() == 0:
        app.contact.add(contact)
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    """удаление первого элемента, т.к. индекс 0-включается,а 1-не включается"""
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

