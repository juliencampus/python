from Character import Character

class Archer(Character) :
    def __init__(self, nom):
        Character.__init__(self, nom)
        self.vie *= 1.2
        self.armo *= 0.8
        self.magarmo *= 0.8
