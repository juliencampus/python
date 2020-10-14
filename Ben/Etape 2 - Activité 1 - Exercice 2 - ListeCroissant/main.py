import random


def main():
    liste = []
    i = 0
    e = 1000
    while i < e: # Tant que i est inferieur a e
        liste.append(random.randint(0,1000)) # Ajoute de façon aléatoire un int entre 0 et 1000
        i += 1

    print(liste) # Affiche des nombres aléatoire entre 0 et 1000
    liste.sort() # Range dans l'ordre croissaant
    print(liste) # Affiche les nombres dans l'ordre croissant


main()