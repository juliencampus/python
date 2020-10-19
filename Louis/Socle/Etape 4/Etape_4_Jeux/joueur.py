import random

class Joueur(object):
    def __init__(self):
        self.vie = 200
        self.experience = self.vie
        self.attPhy = random.randint(10, 20)
        self.attMg = random.randint(10, 20)
        self.armPhy = random.randint(5, 15)
        self.armMg = random.randint(5, 15)

class Wizard(Joueur):
    def __init__(self):
        Joueur.__init__(self)
        self.attMg *= 2
        self.armMg = round(self.armMg * 0.8)

class Archer(Joueur):
    def __init__(self):
        Joueur.__init__(self)
        self.vie *= 1.2
        self.armMg = round(self.armMg * 0.8)
        self.armPhy = round(self.armPhy * 0.8)

class Warrior(Joueur):
    def __init__(self):
        Joueur.__init__(self)
        self.attPhy *= 2
        self.armMg = round(self.armMg * 0.7)

