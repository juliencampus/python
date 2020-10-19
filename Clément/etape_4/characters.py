import random
from abc import ABCMeta, ABC, abstractmethod, abstractproperty


class Character(ABC):
    def __init__(self, name):
        self._attack_magic = random.randint(10, 20)
        self._attack_physic = random.randint(10, 20)
        self._shield_magic = random.randint(5, 15)
        self._shield_physic = random.randint(5, 15)
        self._exp = 1
        self._name = str(name).capitalize()
        self._health = 20
        self.is_tired = False

    def string_att(self):
        return print(f'Name: {self.name} | Health: {self.health} | Attack_magic: {self.attack_magic} | Attack_physic: {self.attack_physic}')

    def string_def(self):
        return print(
            f'Name: {self.name} | Health: {self.health} | Shield_magic: {self.shield_magic} | shield_physic: {self.shield_physic}')

    def attack(self, character, option):
        if str(option) == '1':
            print(f'{self._name} lance une attaque magique')
            character.health = (character.shield_magic-self._attack_magic)
        elif str(option) == '2':
            print(f'{self._name} lance une attaque physique')
            character.health = (character.shield_physic-self._attack_physic)
        print(f'{self.name} attaque {character.name}')
        self.is_tired = True


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
        self._attack_magic += value

    @attack_physic.setter
    def set_attack_physic(self, value):
        self._attack_physic += value

    @shield_physic.setter
    def set_shield_physic(self, value):
        self._shield_physic = self._shield_physic + value

    @exp.setter
    def exp(self, value):
        self._exp = self._exp + value

    @health.setter
    def health(self, value):
        self._health = self._health + value


class Wizard(Character):
    def __init__(self, name='Glozarg'):
        super().__init__(name)
        self._attack_magic *= 2
        self._shield_physic = int(self._shield_physic * 0.8)


class Archer(Character):
    def __init__(self, name="Rhiel"):
        super().__init__(name)
        self._health = int(self._health * 1.2)
        self._shield_physic = int(self._shield_physic * 0.8)


class Warrior(Character):
    def __init__(self, name="Börg"):
        super().__init__(name)
        self._attack_physic *= 2
        self._shield_magic = int(self._shield_magic * 0.8)
