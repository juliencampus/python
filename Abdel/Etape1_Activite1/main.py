import math


def prix_produit(prixht, result):
    prixTTC = prixht + ((prixht * result) / 100)
    return prixTTC


def main():
    nom_produit = input("Nom du produit : ")
    prixht = input("Prix HT : ")
    taxe = input("TVA : ")
    nom_produit = str(nom_produit)
    prixht = float(prixht)
    taxe = float(taxe)

    prixTTC = prix_produit(prixht, taxe)
    result = math.ceil(taxe)

    if result % 2 == 1:
        result += 1

    print("Le prix TTC du produit", nom_produit, "est de", prixTTC, "€ (taxes de", result, "%)")


if __name__ == "__main__":
    main()
