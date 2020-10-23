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

def game():
    print('-----------------------------')

    # J'ai voulu faire jouer mon chien mais cela marche pas
    # Chien.aboyer(Chien.premierchien)

class Chien(Animal):
    vitesseMax = 70     # Vitesse max du chien
    nombrePattes = 4    # Nombre de pattes du chien
    exitBoucle = 0      # Attribut qui permettra de boucler tant qu'une erreur de frappe est faite

    def __init__(self, nom, nombrePattes, vitesseMax):
        Animal.__init__(self, nom, nombrePattes, vitesseMax)

    def __str__(self):
        return "{0} {1} {2} ".format(self.nom, self.nombrePattes, self.vitesseMax)

    # Methode pour faire jouer mon chien

    # def aboyer(self, nom, nombrePattes, vitesseMax):
    #     noms = ["", "chien"]
    #     premierchien = Chien(noms, 0, 0 , 0)
    #     aboiement = self.vitesseMax - 10/100
    #     print(aboiement)



    def makeChien(self):
        while Chien.exitBoucle == 0:
            try:
                self.nom = input(f'Le nom de ton chien : ')
                print(f"Ton chien hérite d'Animal, son nom est :", self.nom, "\n Il possède une pointe de vitesse de : ",
                        self.vitesseMax, "\n Il possède", self.nombrePattes, "pattes")
                Chien.exitBoucle += 1
            except TypeError:
                print("ERROR ! Désolé, ton chien ne peut pas être un nombre eheh")
        game()

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
                print(f"Ta poule hérite d'Animal, son nom est :", self.nom,
                      "\n Elle possède une pointe de vitesse de: ",
                        self.vitesseMax, "\n Elle possède", self.nombrePattes, "pattes")
                Poule.exitBoucle += 1
            except TypeError:
                print("ERROR !")
        game()
class Mouche(Animal):
    vitesseMax = 8
    nombrePattes = 6
    exitBoucle = 0

    def __init__(self, nom, nombrePattes, vitesseMax):
        Animal.__init__(self, nom, nombrePattes, vitesseMax)

    def __str__(self):
        return "{0} {1} {2} " . format(self.nom, self.nombrePattes, self.vitesseMax)

    def makeMouche(self):
        while Mouche.exitBoucle == 0:
            try:
                self.nom = input (f'Le nom de ta mouche :')
                print(f"Ta mouche hérite d'Animal, son nom est :", self.nom,
                      "\n Elle possède une pointe de vitesse de: ",
                      self.vitesseMax, "\n Elle possède", self.nombrePattes, "pattes")
                Mouche.exitBoucle += 1
            except TypeError:
                print('ERROR')
        game()

def makeAnimal():
    exitBoucleAnimal = 0
    while exitBoucleAnimal == 0:
        try:
            noms = ["", "chien", "poule", "mouche"]
            choixAnimal = int(input(f'Tape 1 pour créer un chien'
                                    f'\nTape 2 pour créer une poule'
                                    f'\nTape 3 pour créer une mouche (oui oui...)\n'))
            chien = Chien(noms[choixAnimal], 0, 0)
            poule = Poule(noms[choixAnimal], 0, 0)
            mouche = Mouche(noms[choixAnimal], 0, 0)
            exitBoucleAnimal += 1
        except ValueError:
            print("ERROR ! Il faut entrer 1 ou 2")
        except IndexError:
            print('ERROR ! Entre un numéro entre 1 et 3 ... ')

    if choixAnimal == 1:
        Chien.makeChien(chien)
    if choixAnimal == 2:
        Poule.makePoule(poule)
    if choixAnimal == 3:
        Mouche.makeMouche(mouche)