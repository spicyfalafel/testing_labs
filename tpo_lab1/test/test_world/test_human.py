from models.world.human import Human


def test_human_repl_works(data):
    human = data['human']
    assert str(human) == f'[Human with name {human.name}, age {human.age}, height {human.height}]', 'repr не содержит всю информацию'


def test_human_eq_works(data):
    human1 = data['human']
    human2 = Human(human1.name, human1.age, human1.height)
    human3 = Human("Unknown", 2, 3)

    assert human1 == human2, 'Люди 1 и 2 не были равны'
    assert human1 != human3, 'Люди 1 и 3 были равны'

def test_human_jump_works(data):
    """ very important test """
    human = data['human']
    assert human.jump() == str(human) + ' jumps', 'end of the world'
