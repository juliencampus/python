from .Character import Character

class Mage(Character) :
    def __init__(self, nom):
        Character.__init__(self, nom)
        self.mag *= (1 * 1 + 1)
        self.armo *= 0.8
