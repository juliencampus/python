# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import random
import datetime
import time

min = 0
max = 100

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def askNombre(min, max):

    while True:

        phrase = "Trouve le nombre entre "+str(min)+" et "+str(max)+" : "
        nombre = input(phrase)

        try:
            val = int(nombre)
            return int(val)
        except ValueError:
            print("Merci de rentrer un nombre")

def defineLevel():

    while True:

        level = input("Choix du niveau ?")
        try:
            level = int(level)
            if (level > 0 and level < 4):
                max = 10 * pow(10, level)
                return max
        except:
            print("Merci de rentrer un chiffre entre 1 et 3")

def showScore(score):

    tour = 1
    for index, el in enumerate(score):
        if(tour % 2 != 0):
            tour += 1
            print(f'Tour n°{tour}')
        print(f'Joueur : {el["Player"]} Temps : {el["Temps de partie"]} Gagnée : {el["Win"]} Nombre à trouver : {el["Nombre à trouver"]}')

def main():

    tour = 1
    win = False
    player = True
    score = []

    print("=======Choix de la difficulté======")
    print("1: Facile, nombre entre 0 et 100")
    print("2: Moyen, nombre entre 0 et 1 000")
    print("3: Dur, nombre entre 0 et 10 000")

    max = defineLevel()

    while(tour <= 1):

        timeStart = round(time.time())

        nombreATrouver = random.randrange(min, max)

        essai = 0
        joueur = "1" if player else "2"

        print("Tour numéro ", str(tour)+"\n")
        print(f'Joueur {joueur} à toi de jouer ! \n')

        while(essai <= 10):

            nombreSaisi = askNombre(min, max)
            win = False
            essai += 1

            if(nombreSaisi > nombreATrouver):
                print("C'est plus petit !")
            elif(nombreSaisi < nombreATrouver):
                print("C'est plus grand")
            else:
                print("Gagné en", essai, "essais !")
                win = True
                break


            print("Essai numéro :", essai)

        timeStop = round(time.time()) - timeStart
        print(f'Parie jouée en {timeStop} secondes')


        score.append({"Tour":tour, "Player":joueur, "Temps de partie":timeStop, "Win":win, "Nombre à trouver":nombreATrouver})

        # If player 2
        if(not player):
            tour += 1

        player = not player

    showScore(score)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/