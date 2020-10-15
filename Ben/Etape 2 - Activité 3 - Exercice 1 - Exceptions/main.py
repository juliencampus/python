import random
import time

# Ititialisation des joueurs

class Joueur:
    def __init__(self, vies, pseudo):
        self.vies = vies
        self.pseudo = pseudo

# Faire perdre une vie au joueur

    def perdreVie(self):
        self.vies -= 1

# Ititialisation de la partie)

def rejouer():
    gameplay = input(" Press 1 pour rejouer. \n Press 2 pour quitter.\n")

    if int(gameplay) == 2:
        return False
    else:
        return True


class Partie:
    def __init__(self):
        hgain = self.nombre = random.randint(0, 100)
        print(hgain)

    def jouer(self, choixJoueur):
        appreciation = ""
        temps = round(time.time())
        if int(choixJoueur) < self.nombre:
            print(appreciation + "Trop petit !")
            return False
        if int(choixJoueur) > self.nombre:
            print(appreciation + "C'est trop grand !")
            return False
        else:
            print(appreciation + "GG WP DUDE")
            temps_fin = round(time.time())
            temps_partie = temps_fin - temps
            print(temps_partie)
            return True


# Initialisation des deux joueurs

def partiejouer():

    j1 = input("Mr.Joueur1, entre ton pseudo stp : ")
    j2 = input("Mr.Joueur2, entre ton pseudo stp : ")
    joueur1 = Joueur(5, j1)
    joueur2 = Joueur(5, j2)


    # La partie se lance
    joueur = True
    partie = Partie()

    while joueur1.vies > 0 and joueur2.vies > 0:
        choixJoueur = input(f'A toi {joueur1.pseudo if joueur else joueur2.pseudo}, il te reste : {joueur1.vies if joueur else joueur2.vies} vie(s) ! choisi un nombre :')

        if not partie.jouer(choixJoueur):
            if joueur:
                joueur1.perdreVie()
            else:
                joueur2.perdreVie()
        else:
            print('fin de partie')
            break


        joueur = not joueur

    # Nombre de vies restantes à chaque joueur


    print("Nombre de vies restantes à chaque joueur")
    print(joueur1.pseudo + " : " + str(joueur1.vies) + " restantes")
    print(joueur2.pseudo + " : " + str(joueur2.vies) + " restantes")

nbPartie = 3
while nbPartie > 0:
    partiejouer()
    nbPartie -= 1
    r= rejouer()
    if not r:
        break





