
class Human:
    def __init__(self, name, age, height):
        self.age = age
        self.name = name
        self.height = height


    def jump(self):
        return f'{self} jumps'

    def __repr__(self):
        return f'[Human with name {self.name}, age {self.age}, height {self.height}]'

    def __eq__(self, other):
        if isinstance(other, Human):
            return self.age == other.age and self.name == other.name and self.height == other.height
        return False
