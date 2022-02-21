from models.world.supply import Supply
from models.world.flying_interface import FlyingInterface


class FlyingHorse(FlyingInterface):

    def __init__(self, owner=None):
        self.owner = owner
        self.supply = None

    def fly(self, from_loc, to_loc):
        str = f"{self} flying from {from_loc} to {to_loc}"
        if from_loc.remove(self):
            to_loc.add(self)
        else:
            str = f'{self} can\'t fly from this place! loc hasn\'t this horse'
        return str

    def set_supply(self, supply):
        self.supply = supply

    def set_owner(self, owner):
        self.owner = owner

    def __repr__(self):
        return f'[Horse with owner {self.owner} and supply {self.supply}]'

    def __eq__(self, other):
        if isinstance(other, FlyingHorse):
            return self.owner == other.owner and self.supply == other.supply
        return False
