def prix_produit(prixht, taxe):

    prixTTC = prixht + ((prixht * taxe)/100)
    return prixTTC


def main():
    """Le programme principal."""

    #nom_produit = input("Nom du produit : ")  # une chaîne de caractères

    nom_produit = input("Nom du produit : ")
    prixht = input("Prix HT : ")
    taxe = input("TVA : ")
    nom_produit = str(nom_produit)
    prixht = float(prixht)
    taxe = float(taxe)

    # calculer le périmètre
    prixTTC = prix_produit(prixht, taxe)


    print("Le prix TTC du produit", nom_produit, "est de", prixTTC, "€ (taxes de", taxe, "%)")



if __name__ == "__main__":
    main()