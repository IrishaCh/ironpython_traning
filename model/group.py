class Group:

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        return self.name
