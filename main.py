class Character:
    def __init__(self, name, category, level, power, health):
        self.name = name
        self.category = category
        self.level = level
        self.power = power
        self.health = health

    def __str__(self):
        return f'{self.name} ({self.category}) - PWR: {self.power} | HLT: {self.health} | LVL: {self.level}'

    def attack(self):
        print(f'{self.name} attacked...')


knight = Character('Player K 01', 'Knight', 1, 10, 5)
mage = Character('Player M 01', 'Mage', 1, 5, 10)

print(knight)
print(mage)

mage.attack()
