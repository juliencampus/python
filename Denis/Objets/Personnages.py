# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


class Personnage:
    def __init__(self, nom):
        self.vies = 200
        self.nom = nom
        self.attaquePhysique = round(random.randrange(10, 20))
        self.attaqueMagique = round(random.randrange(10, 20))
        self.armurePhysique = round(random.randrange(5, 15))
        self.armureMagique = round(random.randrange(5, 15))

class Wizard(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.attaqueMagique *= 2
        self.armurePhysique -= 0.2 * self.armurePhysique


class Archer(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.vies += 0.2 * self.vies
        self.armurePhysique -= 0.2 * self.armurePhysique
        self.armureMagique -= 0.2 * self.armureMagique

class Warrior(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.attaquePhysique *= 2
        self.attaqueMagique -= 0.2 * self.attaqueMagique

joueur = Warrior("Test")

