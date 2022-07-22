# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastName="Testov", firstName="Ivan", homePhone="homePhone", mobilePhone="mobilePhone",
                      workPhone="workPhone", secondaryPhone="secondaryPhone")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



