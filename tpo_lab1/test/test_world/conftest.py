
@pytest.fixture(scope='module')
def setup():
    return {
        'supply': Supply('supply'),
        'loc1': Location('loc1'),
        'loc2': Location('loc2'),
        'human': Human('human', 5, 250)
        'horse': FlyingHorse()
    }


@pytest.fixture(scope='function', name='data')
def connect_human_loc_horse(setup):
    setup['loc1'].add(setup['human'])
    horse = setup['horse']
    horse.set_supply(setup['supply'])
    setup['loc1'].add(horse)
    return setup
