import random


class Character:

    def __init__(self, nom):
        self.nom = nom
        self.vie = 200
        self.atk = random.randint(10, 20)
        self.mag = random.randint(10, 20)
        self.armo = random.randint(5, 15)
        self.magarmo = random.randint(5, 15)


class Archer(Character) :
    def __init__(self, nom):
        Character.__init__(self, nom)
        self.vie *= 1.2
        self.armo *= 0.8
        self.magarmo *= 0.8


class Mage(Character) :
    def __init__(self, nom):
        Character.__init__(self, nom)
        self.mag *= (1 * 1 + 1)
        self.armo *= 0.8


class Guerrier(Character) :
    def __init__(self, nom):
        Character.__init__(self, nom)
        self.atk *= (1 * 1 + 1)
        self.magarmo *= 0.7







