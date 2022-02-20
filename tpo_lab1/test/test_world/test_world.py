
def test_horse_str_works(data):
    assert str(data['horse']).contains(str(data['supply'])), 'Не содержит описания supply' 

def test_loc_add_works(data):
    assert data['loc1'].is_in_loc(data['horse']), 'В локации не было лошади'

def test_horse_fly_should_handle_locations(data):
    loc1 = data['loc1'] # в ней лошадь
    loc2 = data['loc2']
    horse = data['horse']

    horse.fly(loc1, loc2)
    assert loc1.is_in_loc(horse) == False, 'Лошадь осталась в начальной локации'
    assert loc2.is_in_loc(horse) == True, 'Лошади нет в конечной локации'


def test_horse_fly_should_handle_uncorrect_locs(data):
    loc1 = data['loc1'] # в ней лошадь
    loc2 = data['loc2']
    horse = data['horse']

    horse.fly(loc2, loc1)
    assert loc1.is_in_loc(horse) == True, 'Лошади нет в начальной локации'
    assert loc2.is_in_loc(horse) == False, 'Лошадь есть в конечной локации'



