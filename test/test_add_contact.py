# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    if symbols[-1] == " ":
        symbols[0:-1]
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstName="", lastName="", homePhone="", mobilePhone="", workPhone="", secondaryPhone="",
                    address="", email="", email2="", email3="")] + \
           [Contact(lastName=random_string('lastName', 10), firstName=random_string('firstName', 20),
                    homePhone=random_string('homePhone', 20), mobilePhone=random_string('mobilePhone', 20),
                    workPhone=random_string('workPhone', 20), secondaryPhone=random_string('secondaryPhone', 20),
                    address=random_string('address', 20), email=random_string('email', 20),
                    email2=random_string('email2', 20), email3=random_string('email3', 20))
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



