import pytest
from models.world.supply import Supply
from models.world.location import Location
from models.world.human import Human
from models.world.horse import FlyingHorse


@pytest.fixture(scope='function')
def setup():
    return {
        'supply': Supply('supply', 1),
        'loc1': Location('loc1'),
        'loc2': Location('loc2'),
        'human': Human('human', 5, 250),
        'horse': FlyingHorse()
    }


@pytest.fixture(scope='function', name='data')
def connect_human_loc_horse(setup):
    human = setup['human']
    setup['loc1'].add(human)
    horse = setup['horse']
    horse.set_supply(setup['supply'])
    setup['loc1'].add(horse)
    horse.set_owner(human)
    return setup
