import random
import string

from Personnages import *

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def showAttributes(perso: object) -> object:

    print(f'Attribut du personnage : \n \
            Nom : {perso.nom} \n \
            Attaque Physique : {perso.attaquePhysique} \n \
            Attaque Magique : {perso.attaqueMagique} \n \
            Armure Physique : {perso.armurePhysique} \n \
            Armure Magique : {perso.armureMagique}')

def createEnnemis():

    return [Warrior(get_random_string(10)) if random.randint(0, 10) < 3 else Wizard(get_random_string(10)) if random.randint(0, 10) < 5 else Archer(get_random_string(10)) for el in range(0, 5)]

def createPerso():

    types = ["Wizard", "Archer", "Warrior"]

    [print(f' {el} \n') for el in types]


    while True:
        type = input("Type du perso ?")
        try:
            type = int(type)
            if(type > 0 and type < 4):
                break
        except:
            print("Mauvais choix")

    nom = input("Son nom ?")

    if type == 1:
        return Wizard(nom)
    elif type == 2:
        return Archer(nom)
    elif type == 3:
        return Warrior(nom)
