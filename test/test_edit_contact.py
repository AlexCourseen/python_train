from model.contact import Contact


def test_edit_contact_firstName(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstName='Edit')
    contact.id = old_contacts[0].id
    contact.lastName = old_contacts[0].lastName
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(firstName='testIvan'))
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_lastName(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastName="Editovich")
    contact.id = old_contacts[0].id
    contact.firstName = old_contacts[0].firstName
    if app.contact.count_contacts() == 0:
        app.contact.add(lastName='testIvanovich')
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


