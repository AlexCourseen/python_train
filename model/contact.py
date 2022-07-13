from sys import maxsize


class Contact:

    def __init__(self, firstName=None, lastName=None, id=None):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    # переопределение функции вывода на косоль - repr
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstName, self.lastName)

    # переопределение стандартной функции - eq, где other - объект с которым сранивать текущий объект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstName == other.firstName and self.lastName == other.lastName

