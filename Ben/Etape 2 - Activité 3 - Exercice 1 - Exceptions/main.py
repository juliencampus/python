import random


class joueur:
    def __init__(self, vies, pseudo):
        self.vies = vies
        self.pseudo = pseudo

    def jouer(self):
        appreciation = ""
        n = random.randint(0, 100)
        while self.vies > 0:
            message = appreciation + "A toi ---> " + self.pseudo + ": " + str(self.vies) + " vies restantes.\n Nombre choisi:"
            var = input(message)
            var = int(var)
            if var < n:
                appreciation = "Trop petit !"
            else:
                appreciation = "Trop grand !"
            if var == n:
                print(f"Nice dude GG WP, il te restait : {self.vies} de vie(s).")
                break
            self.vies -= 1


# Initialisation des deux joueurs

j1 = input("Mr.Joueur1,entre ton pseudo stp : ")
j2 = input("Mr.Joueur2,entre ton pseudo stp : ")
j1 = joueur(5, j1)
j2 = joueur(5, j2)


# Player 1 et Player 2 jouent


j1.jouer()
j2.jouer()

# Nombre de vies restantes à chaque joueur


print("Nombre de vies restantes à chaque joueur")
print(j1.pseudo + " : " + str(j1.vies) + " restantes")
print(j2.pseudo + " : " + str(j2.vies) + " restantes")

# Résultat de la partie


print("------------Résultat de la partie-------------")
if j1.vies > j2.vies:
    print(j1.pseudo + " a gagné la partie")

elif j1.vies == j2.vies:
    print("match nul")

else:
    print(j2.pseudo + " a gagné la partie")
