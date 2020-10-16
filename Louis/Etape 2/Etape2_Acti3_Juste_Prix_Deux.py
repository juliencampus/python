# import
import random
import time
from terminaltables import AsciiTable


def main():

    # ---- Globals Variables

    nombre_tour = 5

    # ---- Dictionary

    dict_level = {1: {'mes': "Vous avez choisis le niveau Facile", 'mes_tour' : '10'},
                  2: {'mes': "Vous avez choisis le niveau Normal", 'mes_tour' : '100'},
                  3: {'mes': "Vous avez choisis le niveau Difficile, t'y es fou !", 'mes_tour' : '1000'}}

    Dashboard_gamer = {1: {'nom': "inconnu", 'score': 0, 'temps': 0},
                       2: {'nom': "inconnu", 'score': 0, 'temps': 0}}


    # ---- Functions

    # ---- Functions/ Choice level

    def choice_level(x):
        if x == 1:
            return random.randint(1, 10)
        elif x == 2:
            return random.randint(1, 100)
        elif x == 3:
            return random.randint(1, 1000)
        else:
            return print('ntm')

    # ---- Functions/ Start tour

    def start_tour(nbG):

        # ---- Functions/ Start tour/ Random number
        dict_level[x]['level'] = choice_level(x)
        nombre_inconnu = dict_level[x]['level']

        # ---- Functions/ Start tour/ Init variable locale
        time_start = round(time.time())
        essais_utilisateur_restant = 10
        saisie_nombre = 0

        print(f"C'est à {Dashboard_gamer[nbG]['nom']} de jouer")

        # ---- Functions/ Start tour/ Init variable local

        while saisie_nombre != nombre_inconnu and essais_utilisateur_restant != 0:
            try:
                saisie_nombre = int(input(f"Saisir un nombre entre 0 et {dict_level[x]['mes_tour']} :"))
                if nombre_inconnu > saisie_nombre:
                    print("[Vincent Lagaf'] : C'est plus !")
                    essais_utilisateur_restant = essais_utilisateur_restant - 1
                    print("[Bill] : Il vous reste ", essais_utilisateur_restant, " essais de réponse")
                elif nombre_inconnu < saisie_nombre:
                    print("[Vincent Lagaf'] : C'est moins.")
                    essais_utilisateur_restant = essais_utilisateur_restant - 1
                    print("[Bill] : Il vous reste ", essais_utilisateur_restant, " essais de réponse")
                else:
                    print("\n[Vincent Lagaf'] : C'est gagné pour ce tour")
                    Dashboard_gamer[x]['score'] = Dashboard_gamer[x]['score'] +1
                    print(f"\n[Vincent Lagaf'] : Votre score est de {Dashboard_gamer[x]['score']} manche(s) remportée, Joeur {Dashboard_gamer[x]['nom']}.")
            except ValueError:
                print("[Vincent Lagaf'] : Noooooooooon ça n'est pas un putain de nombre entier ! Please try again.")
                essais_utilisateur_restant = essais_utilisateur_restant - 1
                print("[Bill] : Il vous reste ", essais_utilisateur_restant, " essais de réponse")

        if essais_utilisateur_restant == 0:
            print("[Vincent Lagaf'] : C'est perdu pour ce tour, gros nul !")
            print(f"\n[Vincent Lagaf'] : Votre score est de {Dashboard_gamer[x]['score']} manche(s) remportée, Joeur {Dashboard_gamer[x]['nom']}.")

        time_end = round(time.time())
        Dashboard_gamer[x]['temps'] = abs(time_start - time_end)
        print("\n[Vincent Lagaf'] : Le nombre inconnu était", nombre_inconnu)
        print(f'\n[Bill] : Le tour à durée {abs(time_start - time_end)} s')




        # if tour_gagné >= 2:
        #     print("[Vincent Lagaf'] : Vous gagniez la vitrine !")
        # else:
        #     print("[Vincent Lagaf'] : Rentre chez toi bouilleur d'enfant.")


    # ---- Program

    # ---- Program/ Choice level
    x = int(input(f'Quel niveau difficulté?\n1:Facile\n2:Moyen\n3:Difficile\n'))
    dict_level[x]['level'] = choice_level(x)
    print(f"Vous avez choisis le niveau {dict_level[x]['mes']}")

    # ---- Program/ Name gamer
    Dashboard_gamer[1]['nom'] = str(input('Le joueur inconnu n°1 doit se nommer\n'))
    print(f'Bonjour Mme/Mme {Dashboard_gamer[1]["nom"]}')

    Dashboard_gamer[2]['nom'] = str(input('Le joueur inconnu n°2 doit se nommer\n'))
    print(f'Bonjour Mme/Mme {Dashboard_gamer[2]["nom"]}')

    # ---- Program/ Start party

    while nombre_tour != 0:
        print("Il vous reste ", nombre_tour, " nombres de tours")
        start_tour(1)
        start_tour(2)
        nombre_tour -=1

    Final_Dashboard = [
        [f'{Dashboard_gamer[1]["nom"]}', f'{Dashboard_gamer[2]["nom"]}'],
        [f'{Dashboard_gamer[1]["score"]}', f'{Dashboard_gamer[2]["score"]}'],
        ['row2 column1', 'row2 column2'],
        ['row3 column1', 'row3 column2']
    ]

    table = AsciiTable(Final_Dashboard)
    print(table.table)










































if __name__ == "__main__":
    main()
