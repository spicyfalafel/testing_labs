
class Location:

    def __init__(self, loc_name, in_loc=None):
        self.loc_name = loc_name
        if in_loc:
            self.in_loc = in_loc
        else:
            self.in_loc = []

    def add(self, something):
        self.in_loc.append(something)

    def is_in_loc(self, something):
        return something in self.in_loc

    def remove(self, something):
        if self.is_in_loc(something):
            self.in_loc.remove(something)
            return True
        return False

    def __repr__(self):
        return f'[Location with name {self.loc_name} and in loc: {self.in_loc}]'
