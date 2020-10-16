def main():
    chaine_etudiants = """213615200;BESNIER;JEAN/213565488;DUPOND;MARC/214665555;DURAND;JULIE"""
    result = {}

    for x in chaine_etudiants.split('/'):
        # print(x) #Separation des etudiants
        donnés_etudiant = x.split(";")
        # print(donnés_etudiant) #Separation des infos de l'etudiant
        result.update({donnés_etudiant[0]: donnés_etudiant[1] + " " + donnés_etudiant[2]})
    print(result)
    return result

    # # Methode a lire de droite a gauche
    # print({x.split(";")[0]: x.split(";")[1] + ' ' + x.split(";")[2] for x in chaine_etudiants.split("/")})


if __name__ == '__main__':
    main()
