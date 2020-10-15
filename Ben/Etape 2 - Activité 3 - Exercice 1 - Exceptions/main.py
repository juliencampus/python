import random


class joueur:
    def __init__(self, vies, pseudo):
        self.vies = vies
        self.pseudo = pseudo

    def jouer(self):
        appreciation = "?"
        n = random.randint(0, 100)
        while self.vies > 0:
            message = appreciation + " A toi " + self.pseudo + " : " + str(self.vies) + "vies restantes. Nombre choisi:"
            var = input(message)
            var = int(var)
            if var < n:
                appreciation = "Trop petit ! "
                print(self.vies, var, appreciation)
            else:
                appreciation = "Trop grand ! "
                print(self.vies, var, appreciation)
            if var == n:
                appreciation = "Nice dude GG WP"
                print(self.vies, var, appreciation)
                break
            self.vies -= 1
# Initialisation des deux joueurs


joueur1 = joueur(10, "player 1")
joueur2 = joueur(10, "player 2")

# Player 1 et Player 2 jouent


joueur1.jouer()
joueur2.jouer()

# Nombre de vies restantes à chaque joueur


print("Nombre de vies restantes à chaque joueur")
print(joueur1.pseudo + " : " + str(joueur1.vies) + " restantes")
print(joueur2.pseudo + " : " + str(joueur2.vies) + " restantes")

# Résultat de la partie


print("Résultat de la partie")
if joueur1.vies < joueur2.vies:
    print(joueur1.pseudo + "a gagné la partie")

elif joueur1.vies == joueur2.vies:
    print("match nul")

else:
    print(joueur2.pseudo + " a gagné la partie")
