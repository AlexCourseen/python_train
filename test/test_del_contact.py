from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(firstName='testIvan'))
    app.contact.delete_first_contact()

