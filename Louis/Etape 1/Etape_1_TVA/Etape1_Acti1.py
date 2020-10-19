

import math

def tarif_ttc(tarif_ht, pourcentage_taxes, quantité_stock):

    print("TVA à l'arrondie sup.", pourcentage_taxes)
    calcul_ttc = tarif_ht / 100 * pourcentage_taxes + tarif_ht * quantité_stock
    return round(calcul_ttc)


def main():
    saisie_nom = input("Nom du produit : ")
    nom_produit = (saisie_nom)

    saisie_tarif_ht = input("Tarif HT du produit : ")
    tarif_ht = float(saisie_tarif_ht)

    saisie_pourcentage_taxes = input("Le pourcentage de taxes à appliquer : ")
    pourcentage_taxes = math.ceil(float(saisie_pourcentage_taxes))

    saisie_quantité_stock = input("La quantité de stock disponible : ")
    quantité_stock = int(saisie_quantité_stock)

    prix_ttc = tarif_ttc(tarif_ht, pourcentage_taxes, quantité_stock)

    if prix_ttc > 1000:
        prix_ttc = prix_ttc * 0.88
        remise_accordée = math.ceil(prix_ttc - (prix_ttc * 0.88))
        print("Le total TTC du stock", nom_produit, "est de", prix_ttc, "€ (taxes de", pourcentage_taxes, "% - remise de", remise_accordée, "€)")
    if prix_ttc < 1000:
        print("Le prix TTC du produit", nom_produit, "est de", prix_ttc, "€ (TVA de", pourcentage_taxes, "%)")
if __name__ == "__main__":
    main()