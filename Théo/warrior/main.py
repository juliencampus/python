from Game import Game
from Character import *
import printer

def pick_teams(game: Game):
    for j, x in enumerate(game.teams):
        print(f"JOUEUR {1+j} CHOISIS SON EQUIPE (JOUEUR {2 if j==0 else 1} TU REGARDE PAS)")
        for i, el in enumerate(x):
            choice = printer.ask(f"""
    Qui veux-tu mettre en position {i} ?
    0 - un GUERRERERER
    1 - un MAGE
    2 - un ARCHER
    """, [0, 1, 2])
            if choice == 0:
                game.place(j,i, Guerrier("guerrier"))
            elif choice == 1:
                game.place(j, i, Mage("mage"))
            elif choice == 2:
                game.place(j, i, Archer("Archer"))

choice = printer.ask("Commencer partie ? Y/N", ["y", "n"])
if choice == "y":
    game = Game()
    pick_teams(game)
    game.print_teams()


