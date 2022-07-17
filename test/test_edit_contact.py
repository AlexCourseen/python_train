from model.contact import Contact
from random import randrange


def test_edit_contact_firstName(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(firstName='testIvan'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstName='Edit')
    contact.id = old_contacts[index].id
    contact.lastName = old_contacts[index].lastName
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    old_contacts[index] = contact
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_lastName(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(lastName='testIvanovich')
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastName="Editovich")
    contact.id = old_contacts[index].id
    contact.firstName = old_contacts[index].firstName
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


