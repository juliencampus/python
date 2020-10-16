import random


def main():
    list_random = []
    i = 0
    while i < 10:
        #ajoute un int (comprsie entre 0 et 1000)  à la fin de la liste, jusqu'a ce qu'on arrive à l'index 10
        list_random.append(random.randint(0, 1000))
        i += 1
        # tri dans l'ordre croissant
        list_random.sort()
        print(list_random)

if __name__ == "__main__":
    main()
