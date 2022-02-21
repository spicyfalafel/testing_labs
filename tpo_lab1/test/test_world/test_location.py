from models.world.horse import FlyingHorse

def test_loc_add_works(data):
    assert data['loc1'].is_in_loc(data['horse']), 'В локации не было лошади'


def test_is_in_loc_works(data):
    loc = data['loc1']
    assert data['human'] in loc.in_loc, 'Не содержит человека'
    assert data['horse'] in loc.in_loc, 'Не содержит лошади'

def test_remove_works(data):
    loc = data['loc1']
    human = data['human']
    horse = data['horse']

    assert loc.is_in_loc(human)
    assert loc.is_in_loc(horse)
    loc.remove(human)
    assert loc.is_in_loc(horse)
    assert not loc.is_in_loc(human)
    loc.remove(horse)
    assert len(loc.in_loc) == 0
