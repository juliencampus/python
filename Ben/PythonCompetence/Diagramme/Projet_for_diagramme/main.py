
class Animal:
    def __init__(self, nom):
        self.nom = nom
        self.age

    def __str__(self):
        return "{0} {1} ".format(self.nom, self.age)


class Chien(Animal):

    def __init__(self, nom, vitessemax):
        Animal.__init__(self, nom)
        self.vitessemax = vitessemax

    def __str__(self):
        return "{0} {1} ".format(self.nom, self.vitessemax)


    def makeChien():
        nom = input(f'Le nom de ton chien : ')
        age = input(f"Entre l'age de ton chien :")
        print(f"Ton chien hérite de Animal, son nom est", nom, 'et a :', age, 'ans.')
        return nom, age



class Chat(Animal):

    def __init__(self, nom, vitessemax):
        Animal.__init__(self, nom)
        self.vitessemax = vitessemax

    def __str__(self):
        return "{0} {1} ".format(self.nom, self.vitessemax)


    def makeChat():
        nom = input(f'Le nom de ton chat : ')
        age = input(f"Entre l'age de ton chat :")
        print(f"Ton chat hérite de Animal, son nom est :", {nom}, 'et a :', {age}, 'ans.')
        return nom, age


def makeAnimal():
    choix = int(input(f'Tape 1 pour créer un chien : \nTape 2 pour créer un chat : '))
    if choix == 1:
        Chien.makeChien()
    elif choix == 2:
        Chat.makeChat()


if __name__ =="__main__":
    makeAnimal()