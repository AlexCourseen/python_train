from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

# переопределение метода вывода на косоль - repr
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)
#переопределение стандартной функции, где other - объект с которым сранивать текущий объект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

