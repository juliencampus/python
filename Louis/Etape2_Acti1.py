def main():

    ma_liste_entier = [13, 15, 89, 68, 2, 9, 87, 65, 2]
    valeur = 2

    index1_valeur_dans_liste = ma_liste_entier.index(valeur)
    print(index1_valeur_dans_liste)

    index2_valeur_dans_liste = ma_liste_entier[index1_valeur_dans_liste+1:].index(valeur)+1
    index_2_occurence = index2_valeur_dans_liste + index1_valeur_dans_liste

    print(index_2_occurence + 1)
    print(index2_valeur_dans_liste)


    ocurrence_valeur = ma_liste_entier.count(valeur)
    print("Le nombre d'occurence de la valeur dans la liste est ", ocurrence_valeur)




if __name__ == "__main__":
    main()