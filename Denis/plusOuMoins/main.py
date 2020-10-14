# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import random

min = 0
max = 1000

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def askNombre(min, max):
    phrase = "Trouve le nombre entre "+str(min)+" et "+str(max)+" : "
    nombre = input(phrase)

    try:
        val = int(nombre)
        return int(val)
    except ValueError:
        print("Merci de rentrer un nombre")
        askNombre(min, max)


def main():

    tour = 0
    win = 0

    while(tour < 3):

        nombreATrouver = random.randrange(min, max)

        essai = 0

        print("Tour numéro ", tour)
        print()
        print()

        while(essai <= 10):

            nombreSaisi = askNombre(min, max)

            if(nombreSaisi > nombreATrouver):
                print("C'est plus petit !")
            elif(nombreSaisi < nombreATrouver):
                print("C'est plus grand")
            else:
                print("Gagné en", essai, "essais !")
                win += 1
                break

            essai+=1
            print("Essai numéro :", essai)


        tour+=1

    if(win > 1):
        print("Gagné !")
    else:
        print("Perdu")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
