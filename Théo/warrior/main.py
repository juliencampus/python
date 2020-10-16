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

def play(game):
    for x in range(0,game.TEAM_SIZE):
        while game.teams[0][x] != 0 and game.teams[1][x] != 0:
            char_t1 = game.teams[0][x]
            char_t2 = game.teams[1][x]
            choice = printer.ask(f"{char_t1.nom}({0}) attaque {char_t2.nom}({1} - (M)agique ou (P)hysique ? ", ["m", "p"])
            if choice == "p":
                attackphy(char_t1, char_t2)
            else:
                attackmag(char_t1, char_t2)

            choice = printer.ask(f"{char_t2.nom}({1}) attaque {char_t1.nom}({0} - (M)agique ou (P)hysique ? ",
                                 ["m", "p"])
            if choice == "p":
                attackphy(char_t2, char_t1)
            else:
                attackmag(char_t2, char_t1)

            if char_t1.vie <= 0:
                game.pop_char(0,x)
                print(f"{char_t1.nom} est mort comme une merde")
            if char_t2.vie <= 0:
                game.pop_char(1, x)
                print(f"{char_t2.nom} est mort comme une merde")




choice = printer.ask("Commencer partie ? Y/N", ["y", "n"])
if choice == "y":
    game = Game()
    pick_teams(game)
    game.print_teams()
    play(game)
    game.print_teams()


