import random


# Ititialisation des joueurs

class Joueur:
    def __init__(self, vies, pseudo):
        self.vies = vies
        self.pseudo = pseudo

# Faire perdre une vie au joueur

    def perdreVie(self):
        self.vies -= 1

# Ititialisation de la partie)

class Partie:
    def __init__(self):
        self.nombre = random.randint(0, 100)

    def jouer(self, choixJoueur):
        appreciation = ""
        if int(choixJoueur) < self.nombre:
            return appreciation + "Trop petit !"
        if int(choixJoueur) > self.nombre:
            return appreciation + "C'est trop grand !"
        else:
            print(appreciation + "GG WP DUDE")
            exit()








# Initialisation des deux joueurs

j1 = input("Mr.Joueur1, entre ton pseudo stp : ")
j2 = input("Mr.Joueur2, entre ton pseudo stp : ")
j1 = Joueur(5, j1)
j2 = Joueur(5, j2)


# La partie se lance
joueur = True
partie = Partie()

while j1.vies > 0 and j2.vies > 0:
    nombre = input(f'A toi {j1.pseudo if joueur else j2.pseudo}, il te reste : {j1.vies if joueur else j2.vies} vie(s) ! choisi un nombre :')

    if print(partie.jouer(nombre)) != 0:

        if joueur:
            j1.perdreVie()
        else:
            j2.perdreVie()

    joueur = not joueur

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
