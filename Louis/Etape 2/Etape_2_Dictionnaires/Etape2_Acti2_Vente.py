

def main():
    ventes = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}

    # Somme des Ventes

    # # 1ère méth
    # Sum_Ventes = 0
    # for x in ventes.values():
    #     Sum_Ventes = Sum_Ventes + x
    # print(Sum_Ventes)
    #
    # # 2ème méth
    # Sum_Ventes = sum(ventes.values())
    # print(Sum_Ventes)

    # 3ème méth
    # Sum_Ventes = {x: sum(x) for x in ventes.values()}
    # print(Sum_Ventes)

    # # Nom de la personne qui à fait le plus de vente
    # Max_Ventes = max(ventes, key = lambda k: ventes[k])
    # print(Max_Ventes)

    # Chaîne étudiants
    chaine_etudiants = """213615200;BESNIER;JEAN
    213565488;DUPOND;MARC
    214665555;DURAND;JULIE"""

    print({str.split(";")[0]: str.split(";")[1] + " " +  str.split(";")[2] for str in chaine_etudiants.split('\n')})

    # Fonction qui je sais pas encore trop à quoi elle va servir

    def jesaispo():
        e = "Je crois ne pas avoir compris l'exercice demandé, a+"
        print(e)

if __name__ == "__main__":
    main()