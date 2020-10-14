# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
def fillListe():

    liste = []
    nb = random.randrange(100, 1000)

    for i in range(nb):
        liste.append(random.randrange(0, 1000))

    return liste

def sortList(liste, reverse = False):

      return sorted(liste, key=None, reverse=reverse)

def main():
    liste = fillListe()

    print(f'Liste ordonnée : {sortList(liste)}')
    print(f'La même à l\'envers : {sortList(liste, True)}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
