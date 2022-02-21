
class Supply:

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return f'Supply {self.name}, count: {self.count}'

    def __eq__(self, other):
        if isinstance(other, Supply):
            return self.name == other.name and self.count == other.count
        return False
