import random

def main():
    nombre_tour = 3
    tour_gagne = 3

    while nombre_tour != 0:

        nombre_inconnu = random.randint(1, 100)
        saisie_nombre = 0
        essai_utilisateur_restant = 10
        print("Il vous reste ", nombre_tour, " nombres de tours")

        while saisie_nombre != nombre_inconnu and essai_utilisateur_restant != 0:
            try:
                saisie_nombre = int(input("Saisir un nombre entre 0 et 100 :"))
                if nombre_inconnu > saisie_nombre:
                    print("[Le programme'] : C'est plus !")
                    essai_utilisateur_restant = essai_utilisateur_restant - 1
                    print("Il vous reste ", essai_utilisateur_restant, " essais")
                elif nombre_inconnu < saisie_nombre:
                    print("[Le programme'] : C'est moins.")
                    essai_utilisateur_restant = essai_utilisateur_restant - 1
                    print("Il vous reste ", essai_utilisateur_restant, " essais")
                else:
                    print("[Le programme'] : C'est gagné pour ce tour")
                    break
                    nombre_tour = nombre_tour - 1
            except ValueError:
                print("[le programme'] : Non des chiffres... Please try again.")
                essai_utilisateur_restant = essai_utilisateur_restant - 1
                print("Il vous reste ", essai_utilisateur_restant, " essais")

        #print("[Le programme'] : C'est perdu pour ce tour!")
        print("[Le programme'] : Le nombre inconnu était", nombre_inconnu)
        nombre_tour = nombre_tour - 1
        tour_gagne = tour_gagne - 1

    if tour_gagné >= 2:
        print("[Le programme'] : Vous gagniez !")
    else:
        print("[le programme'] : dommage, c'est perdu")


if __name__ == "__main__":
    main()