def calculetaxe(nom, leprix):
    prixtaxe = leprix * 0.100
    prixtotal = prixtaxe + leprix
    print("La taxe pour", nom, "est de :", prixtaxe)
    print(nom, "coute maintenant :", prixtotal)

    if leprix > 1000:
        prixtaxe = leprix * 0.100
        prixtotal = prixtaxe + leprix
        reduction = prixtotal * 0.12
        prixtotal = prixtotal - reduction
        print("Ton prix est supérieur à 1000, tu as donc une reduction de 12%")
        print("ton prix total apres reduction est de :", prixtotal)
    else:
        print("inférieur à 1000E, donc pas de réduction")
        prixtaxe = leprix * 0.100
        prixtotal = prixtaxe + leprix


def mesjouets():
    nom: str = input("Saisi le nom de ton produit :")  # Prend le nom du produit
    print("Ok tu veux :", nom)

    prix = input("Selectionne maintenant le prix :")
    leprix = float(prix)
    print("Ton", nom, "coute donc :", leprix, "sans la taxe")
    return calculetaxe(nom, leprix)

mesjouets()