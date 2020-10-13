# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def fillListeFloat():

    liste = []
    nb = 10

    for i in range(nb):
        liste.append(float(random.random() * random.randrange(1, 100)))

    return liste

def fillListe():
    liste = []
    nb = 10

    for i in range(nb):
        liste.append(random.randrange(1, 100))

    return liste

def calculMoyenne(valeur, coef):
    return valeur * coef

def main():
    liste = fillListeFloat()
    coef = fillListe()
    total = 0
    totalCoef = 0

    print(liste)
    print(coef)

    for index, el in enumerate(liste):
        total += el * coef[index]
        totalCoef += coef[index]

    result = total / totalCoef
    print("Moyenne pondérée", result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
