# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from Personnages import *
from Tools import *
from PyQt5.QtWidgets import QApplication, QWidget

def initPerso():
    print("Tes personnages :")
    perso = [createPerso() for el in range(0, 5)]

    [showAttributes(el) for el in perso]


    ennemis = createEnnemis()
    print("Les ennemis générés :")
    [showAttributes(el) for el in ennemis]


def combat():

    tour = 0

    while tour < len(perso):
        print(f'Ton personnage {perso[tour].nom} se bat contre {ennemis[tour].nom} \n \
            Tu as {perso[tour].vies} points de vies \n \
            Il a {ennemis[tour].vies} points de vies \n ')

        while perso[tour].vies > 0 and ennemis[tour].vies > 0:
            if random.randint(0, 10) > 2:
                ennemis[tour].vies -= (perso[tour].attaqueMagique + perso[tour].attaquePhysique) - (ennemis[tour].armureMagique + ennemis[tour].armurePhysique)
                print(f'Ton attaque sur l\'ennemi a fonctionné, il lui reste {round(ennemis[tour].vies)}')
            else:
                print("Ton attaque a échoué")

            if random.randint(0, 10) > 2:
                perso[tour].vies -= (ennemis[tour].attaqueMagique + ennemis[tour].attaquePhysique) - (perso[tour].armureMagique + perso[tour].armurePhysique)
                print(f'L\'ennemi a réussi son attaque, il te reste {round(perso[tour].vies)}')
            else:
                print("Son attaque a échoué")

            input("Appuies sur entrai pour le prochain tour")

        tour += 1

app = QApplication.instance()
window = QWidget()

window.show()

app.exec_()
# combat()