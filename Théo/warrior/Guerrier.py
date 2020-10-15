from Character import Character

class Guerrier(Character) :
    def __init__(self, nom):
        Character.__init__(self, nom)
        self.atk *= (1 * 1 + 1)
        self.magarmo *= 0.7

