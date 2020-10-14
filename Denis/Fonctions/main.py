# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def rectangle(longueur, largeur):
    """

    :type largeur: object
    """
    return int((longueur * 2) + (largeur * 2)), int(longueur * largeur)

def cercle(rayon):

    return int(rayon * 2 * math.pi), int(pow(rayon, 2) * math.pi)

def volumeRect(longueur, largeur, hauteur):

    perimetre, aire = rectangle(longueur, largeur)

    return perimetre * hauteur

def volumeCercle(rayon, hauteur):

    perimetre, aire = cercle(rayon)

    return math.pi * pow(rayon, 2) * hauteur

def main():

    largeur = input("Largeur du rectangle ?")
    longueur = input("Longueur du rectangle ?")
    hauteurRect = input("Hauteur du rectangle ?")

    rayon = input("Rayon du cercle ?")
    hauteurCercle = input("Hauteur du cercle ?")

    while True:

        try:
            largeur = int(largeur)
            longueur = int(longueur)
            rayon = int(rayon)
            hauteurRect = int(hauteurRect)
            hauteurCercle = int(hauteurCercle)
            break
        except:
            print("Erreur dans la saisie d'un des paramètres")

    perimetre, aire = rectangle(largeur, longueur)

    perimetreCercle, aireCercle = cercle(rayon)

    volumePave = volumeRect(largeur, longueur, hauteurRect)
    volumeCylindre = volumeCercle(rayon, hauteurCercle)

    print(f'Périmètre du rectangle : {perimetre}, Aire : {aire}')
    print(f'Périmètre du cercle : {perimetreCercle}, Aire du cercle : {aireCercle}')

    print(f'Volume pavé droit : {volumePave}')
    print(f'Volume cylindre : {volumeCylindre}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
