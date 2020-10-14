# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def fillListe():

    liste = []
    nb = random.randrange(100, 1000)

    for i in range(nb):
        liste.append(random.randrange(0, 1000))

    return liste

def isExist(liste, valeur):

    for i in range(len(liste)):
        if liste[i] == valeur:
            return True

    return False

def listeSansDoublon(liste1, liste2):

    liste = []
    doublon = 0

    for i in range(len(liste1) if len(liste1) > len(liste2) else len(liste2)):

        if (i < len(liste1)):
            if(isExist(liste, liste1[i]) == False):
                liste.append(liste1[i])
            else:
                doublon += 1
        if (i < len(liste2)):
            if (isExist(liste, liste2[i]) == False):
                liste.append(liste2[i])
            else:
                doublon += 1

    print("Nombre de doublons :", doublon)

    return liste

def main():

    liste1 = fillListe()
    liste2 = fillListe()

#Work
    print(liste1)
    print(liste2)
    print(len(liste1))
    print(len(liste2))

#listeSansDoublon(liste1, liste2)
    listeRangee = list(set(liste1+liste2))

    print(listeRangee)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
