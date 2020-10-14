# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Ce programme calcule le périmètre d'un cercle dont
# le rayon a été demandé au clavier à l'utilisateur.

import math

def perimetre_cercle(rayon):
    diametre = 2 * rayon
    return math.pi * diametre

def main():
    saisie = input("Rayon ?")
    rayon = float(saisie)
    if(rayon > 0):
        print("Le périmètre du cercle de rayon ", rayon, " est de ", perimetre_cercle(rayon))
    else:
        print("Merci de rentrer un rayon positif")
        main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
