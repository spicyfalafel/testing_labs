from location import Location
from horse import FlyingHorse
from human import Human
from supply import Supply

# Они сидели на мостовой и смотрели с некоторым беспокойством,
# как огромные дети тяжело прыгают по песку, а дикие лошади с
# грохотом везут по небу в Неизведанные Области свежие запасы армированных изгородей.

something = Supply('Свежие запасы армированных изгородей', 1)

unknown = Location('Неизведанные области')
sky = Location("Небо")
mostovaya = Location('Мостовая')
sand = Location('Песок')

child1 = Human("Big Child 1", 5, 250)
child2 = Human("Big Child 2", 6, 290)

sand.add(child1)
sand.add(child2)

child1.jump()
child2.jump()

wild_horse1 = FlyingHorse()
wild_horse2 = FlyingHorse()

sky.add(wild_horse1)
sky.add(wild_horse2)

wild_horse1.set_supply(something)
wild_horse2.set_supply(something)

wild_horse1.fly(sky, unknown)
wild_horse2.fly(sky, unknown)

print(sky.in_loc)
print(unknown.in_loc)
