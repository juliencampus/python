import math


def prix_produit(prixht, taxe, stock_produit):
    prixTotalTTC = (stock_produit * (prixht + ((prixht * taxe) / 100)))
    return prixTotalTTC


def cal_remise(prixTotalTTC, remise):
    return prixTotalTTC - ((prixTotalTTC * remise) / 100)


def main():
    nom_produit = input("Nom du produit : ")
    stock_produit = input("Nombre de stock : ")
    prixht = input("Prix HT : ")
    taxe = input("TVA : ")

    nom_produit = str(nom_produit)
    stock_produit = float(stock_produit)
    prixht = float(prixht)
    taxe = float(taxe)
    remise = 12

    taxe = math.ceil(taxe)

    if taxe % 2 == 1:
        taxe += 1

    prixTotalTTC = prix_produit(prixht, taxe, stock_produit)

    if prixTotalTTC >= 1000:
        prixTotalTTC = cal_remise(prixTotalTTC, remise)
        print(
            f'Le total TTC du stock de {nom_produit} est de {prixTotalTTC} € (dont taxes de {taxe} % - remise de {remise} %)')
    else:
        print("Le total TTC du stock de", nom_produit, "est de", prixTotalTTC, "€ (dont taxes de ", taxe, "%)")


if __name__ == "__main__":
    main()
