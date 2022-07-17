from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    contact = Contact(firstName='testIvan')
    if app.contact.count_contacts() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    """удаление index элемента, т.к. index+1-не включается в удаляемые"""
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

