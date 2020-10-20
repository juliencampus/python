import random


class joueur:

    def __init__(self, vies, pseudo):
        self.vies = vies
        self.pseudo = pseudo

    def jouer(self):
        resultat = ""
        n = random.randint(0, 100)
        while self.vies > 0:
            try:
                message = f'{resultat} {self.pseudo} : {str(self.vies)} vies restantes alor choisi un nombre : '
                var = input(message)
                var = int(var)
                if var < n:
                    resultat = "Resultat est superieur"
                    print(var, resultat)
                else:
                    resultat = "Resultat est inferieur"
                    print(var, resultat)
                if var == n:
                    resultat = " Bravo, tu as trouvé !"
                    print(var, resultat)
                    break
            except ValueError:
                print("Mauvaise saisie, veuillez entré un nombre")

                self.vies -= 1


nom_joueur1 = input("Joueur 1 = Entrer votre nom : ")
joueur1 = joueur(5, nom_joueur1)
nom_joueur2 = input("Joueur 2 = Entrer votre nom  : ")
joueur2 = joueur(5, nom_joueur2)



joueur1.jouer()
joueur2.jouer()

print("Nombre de vies restantes à chaque joueur")
print(f'{joueur1.pseudo} : {str(joueur1.vies)} restantes')
print(f'{joueur2.pseudo} : {str(joueur2.vies)} restantes')

print("Résultat de la partie")
if joueur1.vies < joueur2.vies:
    print(joueur1.pseudo + "a gagné la partie")
elif joueur1.vies == joueur2.vies:
    print("match nul")
else:
    print(joueur2.pseudo + " a gagné la partie")
