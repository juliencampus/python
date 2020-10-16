def main():

    ventes = {"dupont": 14, "hervy": 19, "Geoffrey": 15, "layec": 21}

    # somme des ventes
    # somme_ventes = sum(ventes.values())
    # print(somme_ventes)

    # vendeur ayant réalisé le + de ventes
    best_vendeur = max(ventes, key=ventes.get)
    print(best_vendeur)


    # chaine_etudiants = """213615200;BESNIER;JEAN
    #      213565488;DUPOND;MARC
    #      214665555;DURAND;JULIE"""
    #
    # def dict(string):
    #     dict = {x.split(";")[0]: x.split(";")[1] + ' ' + x.split(";")[2] for x in string.split("\n")}
    #     return (dict)
    #
    # print(dict(chaine_etudiants))


if __name__ == "__main__":
         main()