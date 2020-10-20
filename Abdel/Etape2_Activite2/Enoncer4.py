def main():
    etudiants = {
        'BESNIER': [5, 2, 7],
        'JEAN': [20, 19, 20],
        'DUPOND': [20, 20, 19],
        'MARC': [11, 10, 17],
        'DURAND': [18, 10, 17],
        'JULIE': [14, 10, 14],
    }

    moyenne_etudiant = {}
    resultat = []

    for x in etudiants:
        moyenne_etudiant.update({x: sum(etudiants[x]) / len(etudiants[x])})
    for y in moyenne_etudiant:
        if moyenne_etudiant[y] == moyenne_etudiant[max(moyenne_etudiant)]:
            resultat.append(y)
    print(resultat)

if __name__ == '__main__':
    main()