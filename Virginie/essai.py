import random


def main():
    nombre_tour = 3
    tour_gagne = 3

    while nombre_tour != 0:

        nombre_inconnu = random.randint(1, 1000)
        saisie_nombre = 0
        essais_utilisateur_restant = 10
        print("Il vous reste ", nombre_tour, " nombres de tours")

        while saisie_nombre != nombre_inconnu and essais_utilisateur_restant != 0:
            try:
                saisie_nombre = int(input("Saisir un nombre entre 0 et 1000 :"))
                if nombre_inconnu > saisie_nombre:
                    print("[Vincent Lagaf'] : C'est plus !")
                    essais_utilisateur_restant = essais_utilisateur_restant - 1
                    print("Il vous reste ", essais_utilisateur_restant, " essais de réponse")
                elif nombre_inconnu < saisie_nombre:
                    print("[Vincent Lagaf'] : C'est moins.")
                    essais_utilisateur_restant = essais_utilisateur_restant - 1
                    print("Il vous reste ", essais_utilisateur_restant, " essais de réponse")
                else:
                    print("[Vincent Lagaf'] : C'est gagné pour ce tour")
                    break
                    nombre_tour = nombre_tour - 1
            except ValueError:
                print("[Vincent Lagaf'] : Noooooooooon ça n'est pas un putain de nombre entier ! Please try again.")
                essais_utilisateur_restant = essais_utilisateur_restant - 1
                print("Il vous reste ", essais_utilisateur_restant, " essais de réponse")

        print("[Vincent Lagaf'] : C'est perdu pour ce tour, gros nul !")
        print("[Vincent Lagaf'] : Le nombre inconnu était", nombre_inconnu)
        nombre_tour = nombre_tour - 1
        tour_gagne = tour_gagne - 1

    if tour_gagné >= 2:
        print("[Vincent Lagaf'] : Vous gagniez la vitrine !")
    else:
        print("[Vincent Lagaf'] : Rentre chez toi bouilleur d'enfant.")


if __name__ == "__main__":
    main()