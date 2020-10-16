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
    gameplay = input("| Press 1 pour rejouer.                     | \n"
                     "| Press 2 pour quitter.                     |\n"
                     "---------------------------------------------\n")

    if int(gameplay) == 2:
        return False
    else:
        return True


# Choose level

def choix_niveau():
    choix = int (input(f'Press 1 pour un level easy -> Nombre entre 0 et 50 \n'
                  f'Press 2 pour un level normal -> Nombre entre 0 et 100 \n'
                  f'Press 3 pour un level hard -> Nombre entre 0 et 1000 \n'))
    try:
        if choix == 1:
            nombre = random.randint(0, 50)
            print(nombre)
        if choix == 2:
            nombre = random.randint(0, 100)
            print(nombre)
        if choix == 3:
            nombre = random.randint(0, 1000)
            print(nombre)

    except ValueError:
        print("Selectionne un chiffre s'il te plait.")


class Partie:
    def __init__(self):
        choix_niveau()

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
        choix_joueur = input(
            f'A toi {joueur1.pseudo if joueur else joueur2.pseudo}, il te reste : {joueur1.vies if joueur else joueur2.vies} vie(s) ! choisi un nombre :')

        if not partie.jouer(choix_joueur):
            if joueur:
                joueur1.perdreVie()
            else:
                joueur2.perdreVie()
        else:
            print('----------------Fin de partie----------------')
            break

        joueur = not joueur

    # Nombre de vies restantes à chaque joueur

    print("| Nombre de vies restantes à chaque joueur  |")
    print("| " + joueur1.pseudo + " avait : " + str(joueur1.vies) + " restantes                    |")
    print("| " + joueur2.pseudo + " avait : " + str(joueur2.vies) + " restantes                    |")


nbPartie = 3
while nbPartie > 0:
    partiejouer()
    nbPartie -= 1
    r = rejouer()
    if not r:
        break
