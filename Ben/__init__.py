def calculetaxe(nom, leprix):
    print("La taxe est de 10% du prix, donc : ")
    prixtaxe = leprix * 0.100
    prixtotal = prixtaxe + leprix
    print("La taxe pour ton", nom, "est de :", prixtaxe)
    print("Ton :", nom, "coute en faite :", prixtotal)


def mesjouets():
    nom: str = input("Saisi le nom de ton produit :")  # Prend le nom du produit
    print("Ok le :", nom)

    prix = input("Selectionne maintenant le prix :")
    leprix = float(prix)
    print("Ton", nom, "coute donc :", leprix, "sans la taxe")
    return calculetaxe(nom, leprix)




mesjouets()
