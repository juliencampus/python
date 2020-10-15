import random


class Character:

    def __init__(self, nom):
        self.nom = nom
        self.vie = 200
        self.atk = random.randint(10, 20)
        self.mag = random.randint(10, 20)
        self.armo = random.randint(5, 15)
        self.magarmo = random.randint(5, 15)

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_vie(self):
        return self._vie

    def set_vie(self, vie):
        self._vie = vie

    def get_atk(self):
        return self._atk

    def set_atk(self, atk):
        self._atk = atk

    def get_mag(self):
        return self._mag

    def set_mag(self, mag):
        self._mag = mag

    def get_armo(self):
        return self._armo

    def set_armo(self, armo):
        self._armo = armo

    def get_magarmo(self):
        return self._magarmo

    def set_magarmo(self, magarmo):
        self._magarmo = magarmo




class Archer(Character) :
    def __init__(self, nom):
        super().__init__(nom)
        self.vie *= 1.2
        self.armo *= 0.8
        self.magarmo *= 0.8


class Mage(Character) :
    def __init__(self, nom):
        super().__init__(nom)
        self.mag *= (1 * 1 + 1)
        self.armo *= 0.8


class Guerrier(Character) :
    def __init__(self, nom):
        super().__init__(nom)
        self.atk *= (1 * 1 + 1)
        self.magarmo *= 0.7


def attackphy(Character, ennemi: Character) :
    ennemi.vie = ennemi.vie - (Character.atk-ennemi.armo)

def attackmag(Character, ennemi: Character) :
    ennemi.vie = ennemi.vie - (Character.mag-ennemi.magarmo)


def die(self) :
    if self.vie < 0 :
        print("DEAD")









