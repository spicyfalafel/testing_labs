from models.world.horse import FlyingHorse


def test_horse_str_works(data):
    assert str(data['supply']) in str(data['horse']), 'Не содержит описания supply'
    assert str(data['human']) in str(data['horse']), 'Не содержит описания owner'


def test_horse_str_without_owner(setup):
    """
    horse без owner и supply
    """
    assert str(setup['supply']) not in str(setup['horse']), 'Cодержит описания supply'
    assert str(setup['human']) not in str(setup['horse']), 'Содержит описание owner'

def test_horse_eq_works(data):
    horse2 = FlyingHorse(owner=data['human'])
    horse3 = FlyingHorse()
    horse2.set_supply(data['supply'])
    assert horse2 == data['horse'], 'Лошади не были равны'
    assert horse3 != data['horse'], 'Лошади 3 и 1 были равны'

def test_horse_fly_should_handle_locations(data):
    loc1 = data['loc1']  # в ней лошадь
    loc2 = data['loc2']
    horse = data['horse']

    horse.fly(loc1, loc2)
    assert loc1.is_in_loc(horse) == False, 'Лошадь осталась в начальной локации'
    assert loc2.is_in_loc(horse) == True, 'Лошади нет в конечной локации'


def test_horse_fly_should_handle_uncorrect_locs(data):
    loc1 = data['loc1']  # в ней лошадь
    loc2 = data['loc2']
    horse = data['horse']

    horse.fly(loc2, loc1)
    assert loc1.is_in_loc(horse) == True, 'Лошади нет в начальной локации'
    assert loc2.is_in_loc(horse) == False, 'Лошадь есть в конечной локации'
