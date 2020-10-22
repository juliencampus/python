
class Animal():
    nom =" "
    nombrePattes = 0
    vitesseMax = 0
    def __init__(self, nom, nombrePattes, vitesseMax):
        self.nom = nom

    def __str__(self):
        return "{0} {1}".format(self.nom, self.nombrePattes)


class Chien(Animal):
    vitesseMax = 70
    nombrePattes = 4

    def __init__(self, nom, nombrePattes, vitesseMax):
        Animal.__init__(self, nom, nombrePattes, vitesseMax)

    def __str__(self):
        return "{0} {1} {2} ".format(self.nom, self.nombrePattes, self.vitesseMax)


    def makeChien(self):
        self.nom = input(f'Le nom de ton chien : ')
        print(f"Ton chien hérite d'Animal, son nom est :", self.nom, "\n Il possède une pointe de vitesse de : ", self.vitesseMax, "\n Il possède", self.nombrePattes, "pattes")



class Poule(Animal):
    vitesseMax = 15
    nombrePattes = 2

    def __init__(self, nom, nombrePattes, vitesseMax):
        Animal.__init__(self, nom, nombrePattes, vitesseMax)

    def __str__(self):
        return "{0} {1} {2} ".format(self.nom, self.nombrePattes, self.vitesseMax)


    def makePoule(self):
        self.nom = input(f'Le nom de ta poule : ')
        print(f"Ta poule hérite d'Animal, son nom est :", self.nom, "\n Elle possède une pointe de vitesse de: ", self.vitesseMax, "\n Elle possède", self.nombrePattes, "pattes")


def makeAnimal():
    noms = ["", "chien", "poule"]
    choixAnimal = int(input(f'Tape 1 pour créer un chien : \nTape 2 pour créer une poule : '))
    chien = Chien(noms[choixAnimal], 0, 0)
    poule = Poule(noms[choixAnimal], 0, 0)
    try:
        if choixAnimal == 1:
            Chien.makeChien(chien)
        elif choixAnimal == 2:
            Poule.makePoule(poule)
    except ValueError:
        print('Entre nombre stp frr')


if __name__ == "__main__":
    makeAnimal()