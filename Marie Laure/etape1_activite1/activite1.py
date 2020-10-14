import math


def calcul_prix_ttc(prix_ht, tva, stock=1):
    """Calcule un prix TTC à partir d'un prix HT et d'un pourcentage de TVA.
        :param prix_ht: entier positif
        :param tva: entier positif
        :param stock: entier positif (par défaut 1)
        :return le prix TTC"""
    return round((prix_ht * (1 + tva / 100)) * stock, 2)


def calcul_tva(prix_ht, tva, stock=1):
    """Calcule le montant de la TVA"""
    return round((prix_ht * (tva / 100)) * stock, 2)


def calcul_remise(montant_stock):
    """Calcule le montant de la remise"""
    return round(montant_stock * (12/100), 2)


def main():
    nom_article = input("Saisir le nom de l'article")

    prix_ht = -1
    while prix_ht < 0:
        prix_ht = input("Quel est le prix HT ?")
        try:
            prix_ht = int(prix_ht)
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            prix_ht = -1
            continue
        if prix_ht < 0:
            print("Vous ne pouvez pas saisir un nombre négatif.")

    tva = -1
    while tva < 0:
        tva = input("Quel est le taux de TVA ?")
        try:
            tva = float(tva)
            tva = math.ceil(tva)
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            tva = -1
            continue
        if tva < 0:
            print("Vous ne pouvez pas saisir un nombre négatif.")

    stock = -1
    while stock < 0:
        stock = input("Quelle est la quantité en stock ?")
        try:
            stock = int(stock)
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            stock = -1
            continue
        if stock < 0:
            print("Vous ne pouvez pas saisir un nombre négatif.")

    prix_ttc = calcul_prix_ttc(prix_ht, tva)
    montant_tva = calcul_tva(prix_ht, tva)
    montant_stock = calcul_prix_ttc(prix_ht, tva, stock)
    montant_tva_stock = calcul_tva(prix_ht, tva, stock)

    print("Le prix unitaire TTC du produit", nom_article, "est de", prix_ttc, "€ (TVA", tva, "%, soit", montant_tva, "€.)")

    if montant_stock >= 1000:
        remise = calcul_remise(montant_stock)
        montant_stock = montant_stock - remise
        print("Le total TTC du stock de", nom_article, "est de", montant_stock, "€ (dont", montant_tva_stock,
              "€ de taxes et", remise, "€ de remise.)")
    else:
        print("Le total TTC du stock de", nom_article, "est de", montant_stock, "€ (dont", montant_tva_stock,
              "€ de taxes.)")


main()
