import re
from random import randrange

def test_contact_details_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstName == contact_from_edit_page.firstName
    assert contact_from_home_page.lastName == contact_from_edit_page.lastName
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                 [contact.homePhone, contact.mobilePhone, contact.workPhone, contact.secondaryPhone]))))

def clear(s):
   return re.sub("[() -]", "", s)
