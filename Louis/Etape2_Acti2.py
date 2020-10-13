

import random




def main():
        nombre_inconnu = random.randint(1, 1000)
        saisie_nombre = 0
        essais_utilisateur_restant = 10
        print("[Vincent Lagaf'] : La partie commence")
        print("[Vincent Lagaf'] : Vous avez ", essais_utilisateur_restant, " proposition de réponses au démarrage")


        while saisie_nombre != nombre_inconnu and essais_utilisateur_restant != 0:

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
                                print("[Vincent Lagaf'] : C'est gagné")
                                break

        print("Gros nul !")




if __name__ == "__main__":
        main()