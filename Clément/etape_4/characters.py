import random

class Character(object):
    def __init__(self, name):
        self._attack_magic = random.randint(10, 20)
        self._attack_physic = random.randint(10, 20)
        self._shield_magic = random.randint(5, 15)
        self._shield_physic = random.randint(5, 15)
        self._exp = 1
        self._name = str(name).capitalize()
        self._health = 200

    def string_chara(self):
        print(f'Name: {self.name}\n'
              f'Health: {self.health}\n'
              f'Exp: {self.exp}\n'
              f'Attack_magic: {self.attack_magic}\n'
              f'Attack_physic: {self.attack_physic}\n'
              f'shield_magic: {self.shield_magic}\n'
              f'shield_physic: {self.shield_physic}\n')


    # getters
    @property
    def attack_magic(self):
        return self._attack_magic

    @property
    def attack_physic(self):
        return self._attack_physic

    @property
    def shield_magic(self):
        return self._shield_magic

    @property
    def shield_physic(self):
        return self._shield_physic

    @property
    def exp(self):
        return self._exp

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    # setters
    @attack_magic.setter
    def attack_magic(self, value):
        self._attack_magic = self._attack_magic + value

    @attack_physic.setter
    def set_attack_physic(self, value):
        self._attack_physic = self._attack_physic + value

    @exp.setter
    def exp(self, value):
        self._exp = self._exp + value

    @health.setter
    def health(self, value):
        self._health = self._health + value







