from sys import maxsize


class Contact:

    def __init__(self, firstName=None, lastName=None, homePhone=None, mobilePhone=None, workPhone=None,
                 secondaryPhone=None, all_phones_from_home_page=None, address=None,email=None, email2=None, email3=None,
                 all_emails_from_home_page=None, id=None):
        self.firstName = firstName
        self.lastName = lastName
        self.homePhone = homePhone
        self.mobilePhone = mobilePhone
        self.workPhone = workPhone
        self.secondaryPhone = secondaryPhone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id
    # переопределение функции вывода на косоль - repr
    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstName, self.lastName, self.all_emails_from_home_page,
                                      self.all_phones_from_home_page, self.address)

    # переопределение стандартной функции - eq, где other - объект с которым сранивать текущий объект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstName == other.firstName and self.lastName == other.lastName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
