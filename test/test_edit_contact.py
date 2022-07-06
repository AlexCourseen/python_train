from model.contact import Contact


def test_edit_contact_(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(firstName='testIvan'))
    app.contact.edit_first_contact(Contact(firstName="Edit"))


def test_edit_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(lastName='testIvanovich'))
    app.contact.edit_first_contact(Contact(lastName="Editovich"))

