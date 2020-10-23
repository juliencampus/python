
# Creation de ma classe Animal :

class Animal():
    nom = " "
    nombrePattes = 0
    vitesseMax = 0

    def __init__(self, nom, nombrePattes, vitesseMax):
        self.nom = nom

    def __str__(self):
        return "{0} {1}".format(self.nom, self.nombrePattes)

# Creation de la classe chien qui hérite d'Animal

class Chien(Animal):
    vitesseMax = 70     # Vitesse max du chien
    nombrePattes = 4    # Nombre de pattes du chien
    exitBoucle = 0      # Attribut qui permettra de boucler tant qu'une erreur de frappe est faite

    def __init__(self, nom, nombrePattes, vitesseMax):
        Animal.__init__(self, nom, nombrePattes, vitesseMax)

    def __str__(self):
        return "{0} {1} {2} ".format(self.nom, self.nombrePattes, self.vitesseMax)

    def makeChien(self):
        while Chien.exitBoucle == 0:
            try:
                self.nom = input(f'Le nom de ton chien : ')
                print(f"Ton chien hérite d'Animal, son nom est :", self.nom, "\n Il possède une pointe de vitesse de : ",
                        self.vitesseMax, "\n Il possède", self.nombrePattes, "pattes")
                Chien.exitBoucle += 1
            except TypeError:
                print("ERROR ! Désolé, ton chien ne peut pas être un nombre eheh")

class Poule(Animal):
    vitesseMax = 15
    nombrePattes = 2
    exitBoucle = 0

    def __init__(self, nom, nombrePattes, vitesseMax):
        Animal.__init__(self, nom, nombrePattes, vitesseMax)

    def __str__(self):
        return "{0} {1} {2} ".format(self.nom, self.nombrePattes, self.vitesseMax)

    def makePoule(self):
        while Poule.exitBoucle == 0:
            try:
                self.nom = input(f'Le nom de ta poule : ')
                print(f"Ta poule hérite d'Animal, son nom est :", self.nom, "\n Elle possède une pointe de vitesse de: ",
                        self.vitesseMax, "\n Elle possède", self.nombrePattes, "pattes")
                Poule.exitBoucle += 1
            except TypeError:
                print("ERROR !")

def makeAnimal():
    exitBoucleAnimal = 0
    while exitBoucleAnimal == 0:
        try:
            noms = ["", "chien", "poule"]
            choixAnimal = int(input(f'Tape 1 pour créer un chien : \nTape 2 pour créer une poule : '))
            chien = Chien(noms[choixAnimal], 0, 0)
            poule = Poule(noms[choixAnimal], 0, 0)
            exitBoucleAnimal += 1
        except ValueError:
            print("ERROR ! Il faut entrer 1 ou 2")
        except IndexError:
            print('ERROR ! Please entre SOIT 1 SOIT 2 abuse pas')

    if choixAnimal == 1:
        Chien.makeChien(chien)
    elif choixAnimal == 2:
        Poule.makePoule(poule)


if __name__ == "__main__":
    makeAnimal()
