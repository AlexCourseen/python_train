from model.contact import Contact


def test_edit_contact_(app):

    app.contact.edit_first_contact(Contact(firstName="Edit"))


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(lastName="Editovich"))

