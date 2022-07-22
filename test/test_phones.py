import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homePhone == clear(contact_from_edit_page.homePhone)
    assert contact_from_home_page.mobilePhone == clear(contact_from_edit_page.mobilePhone)
    assert contact_from_home_page.workPhone == clear(contact_from_edit_page.workPhone)
    assert contact_from_home_page.secondaryPhone == clear(contact_from_edit_page.secondaryPhone)


def test_phone_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homePhone == contact_from_edit_page.homePhone
    assert contact_from_view_page.mobilePhone == contact_from_edit_page.mobilePhone
    assert contact_from_view_page.workPhone == contact_from_edit_page.workPhone
    assert contact_from_view_page.secondaryPhone == contact_from_edit_page.secondaryPhone


def clear(s):
   return re.sub("[() -]", "", s)


