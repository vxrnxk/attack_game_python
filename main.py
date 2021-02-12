from random import randint


class Character:
    def __init__(self, name, category, level, power, health):
        self.name = name
        self.category = category
        self.level = level
        self.power = power
        self.health = health

        if name:
            self.name = name
        else:
            self.name = category + str(randint(1,99))


    def __str__(self):
        return f'{self.name} ({self.category}) - PWR: {self.power} | HLT: {self.health} | LVL: {self.level}'


    def attack(self):
        print(f'{self.name} attacked...')


knight = Character('Player K 01', 'Knight', 1, 10, 5)
mage = Character('Player M 01', 'Mage', 1, 5, 10)
archer = Character(None, 'Archer', 1, 8, 6)

print(knight)
print(mage)
print(archer)

mage.attack()
