from terminaltables import AsciiTable


def main():

    Dashboard_gamer = {1: {'nom': "Maurice", 'score': 200, 'temps': 30},
                       2: {'nom': "Carolle", 'score': 20, 'temps': 24}}

    Final_Dashboard = [
        [f'{Dashboard_gamer[1]["nom"]}', f'{Dashboard_gamer[2]["nom"]}'],
        ['point', 'Score'],
        [f'{Dashboard_gamer[1]["score"]}', f'{Dashboard_gamer[2]["score"]}'],
        ['Temps total', 'Temps total'],
        [f'{Dashboard_gamer[1]["temps"]}', f'{Dashboard_gamer[2]["temps"]}']

    ]

    cles = list(Dashboard_gamer[1].keys())
    print(cles[1])


    table = AsciiTable(Final_Dashboard)
    print(table.table)

if __name__ == "__main__":
    main()