import math
from math import *


def tarif_ttc(prixht, taxe):

    prixttc = prixht + (prixht * math.ceil(taxe) / 100)
    return prixttc


def main():
    """Le programme principal."""
    # demander le rayon à l'utilisateur
    nom_produit = input("Nom du produit : ")  # une chaîne de caractères
    prixht = input("prixht :")
    taxe = input("TVA : ")

    nom_produit = str(nom_produit)  # convertie en un nombre réel
    prixht = float(prixht)
    taxe = float(taxe)

    # calculer le tarif TTC

    prixttc = tarif_ttc(prixht, taxe)
    result = math.ceil(taxe)
    if result % 2 == 1:
        result = result + 1



    # afficher le périmètre à l'utilisateur
    print(f"Le prix TTC de {nom_produit} est de prixttc {prixttc} € (taxe de {result} %)")



if __name__ == "__main__":
    main()

# def print_hi(name):
#
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
