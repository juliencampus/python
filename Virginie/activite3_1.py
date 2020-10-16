import random

class joueur:
    def __init__(self, vies, pseudo):
        self.vies = vies
        self.pseudo = pseudo


    def jouer(self):
        appreciation = "?"
      prixatrover =  n = random.randint(0,100)
        while self.vies > 0:
            message = appreciation + " -- " + self.pseudo + " : " + str(self.vies) + " vies restantes. Nombre choisi : "
            var = input(message)
            var = int(var)
            if var < n :
                appreciation = "trop bas"
                print(self.vies, var, appreciation)
            else :
                appreciation = "trop haut"
                print(self.vies, var, appreciation)
            if var == n:
                appreciation = "bravo !"
                print(self.vies, var, appreciation)
                break

            self.vies -= 1

# Initialisation des deux joueurs
blaz = input("ton blaz : ")
j1 = joueur(5, blaz)
blaz2 = input("ton blaz : ")
j2 = joueur(5, blaz2)

# j1 et j2 jouent
j1.jouer()
j2.jouer()

# Nombre de vies restantes à chaque joueur
print("Nombre de vies restantes à chaque joueur")
print(j1.pseudo  + " : " + str(j1.vies) + " restantes")
print(j2.pseudo  + " : " + str(j2.vies) + " restantes")

# Résultat de la partie
print("Résultat de la partie")
if j1.vies < j2.vies:
    print(j1.pseudo + "a gagné la partie")
elif j1.vies == j2.vies:
    print("match nul")
else: print(j2.pseudo + " a gagné la partie")
