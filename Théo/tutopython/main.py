# Ce programme calcule le périmètre d'un cercle dont
# le rayon a été demandé au clavier à l'utilisateur.

import math

def calcul_prix(un_prix, taxed, qty):
    """Calculer le périmètre d'un cercle à partir de son rayon.
	:param un_rayon: le rayon du cercle (positif)
	:return le périmètre d'un cercle de rayon un_rayon
    """
    arb = taxed / 100 + 1
    tva = math.ceil((arb * un_prix)*qty)
    return  tva


def main():
    """Le programme principal."""
    # demander le prix à l'utilisateur
    nom = input("nom du produit : ")
    saisie = input("Prix : ")    # une chaîne de caractères
    le_prix = float(saisie)  # convertie en un nombre réel
    qtt = input("quantité desirez : ")
    qty = float(qtt)
    taxe = input(" taxe en % : ")
    taxed = math.ceil(float(taxe))

    # calculer le prix

    prix = calcul_prix(le_prix, taxed, qty)

    # afficher le resultat
    print("Le prix TTC du pack de", nom, "est de", float(prix),"€", "pour une quantité de", qty, "taxe à", taxed, "%")

if __name__ == "__main__":
    main()
