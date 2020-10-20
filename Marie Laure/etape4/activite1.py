import random


class Character:

    def __init__(self, name):
        self.health = 200
        self.physical_attack = random.randint(10, 20)
        self.magical_attack = random.randint(10, 20)
        self.shield = random.randint(5, 15)
        self.magical_shield = random.randint(5, 15)
        self.name = str(name).capitalize()


class Wizard(Character):

    def __init__(self, name="Gandlaf"):
        super().__init__(name)
        self.magical_attack *= 2
        self.shield = self.shield * 0.8


class Archer(Character):

    def __init__(self, name="Legolas"):
        super().__init__(name)
        self.health = self.health * 1.2
        self.shield = self.shield * 0.8


class Warrior(Character):

    def __init__(self, name="Gimli"):
        super().__init__(name)
        self.physical_attack *= 2
        self.magical_shield = self.magical_shield * 0.7


# Les magiciens
player1 = Wizard()
player2 = Wizard("Saroumane")


# Les archers
player3 = Archer()
player4 = Archer("Orc")


# Les guerriers
player5 = Warrior()
player6 = Warrior("Lurtz")

print(player1.name)
print(player2.name)
print(player3.name)
print(player4.name)
print(player5.name)
print(player6.name)
print(Warrior.__mro__)







