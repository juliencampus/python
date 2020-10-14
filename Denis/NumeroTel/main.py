# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import random

def menu():

    print("=====MENU======")
    print("L pour lister les numéros")
    print("A pour ajouter un numéro")
    print("S pour supprimer un numéro")
    print("E pour enregistrer")
    print("Q pour quitter")

    while True:

        lettre = input(" ?")
        lettre = lettre.upper()

        if((lettre == 'L' or lettre == 'A' or lettre == 'S' or lettre == 'Q' or lettre == 'E') and lettre.isalpha()):
            return lettre


def renvoieNum(lettre, dic):

    return {d:el for d, el in dic.items() if lettre == d[0]}

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def fillRepertoire(rep):

    return {get_random_string(random.randrange(3, 10)) : str("06"+str(random.randrange(10000000, 99999999)))  for el in range(0, 500)}


def main():
    rep = {}
    rep = fillRepertoire(rep)

    while True:

        men = menu()

        if(men == 'L'):
            lettre = input("Quelle lettre rechercer ?")
            print(f'Numero commencant par {lettre}')
            print(renvoieNum(lettre, rep))

        elif(men == 'A'):
            nom = input("Nom du contact ?")
            numero = input("Numero du contact ?")
            rep[nom] = numero

        elif(men == 'S'):
            for i, el in sorted(rep.items()):
                print(f'{i} : {el} \n')
            suppr = input("Index à supprimer ?")
            del rep[suppr]
            print(f'Numero {suppr} supprimé')

        elif(men == 'E'):
            with open("repertoire.txt", "w") as num:
                for i, el in rep.items():
                    num.write("{} : {}\n".format(i, el))

        elif(men == 'Q'):
            print("Bisous")
            break




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
