import random


def main():
    tour = 3
    tour_gagner = 3
    while tour != 0:
        nombre_a_deviner = random.randint(1, 100)
        nbr_taper = 0
        essai_user = 10
        print(f'Il vous reste {tour} tours')
        victoir = False
        while nbr_taper != nombre_a_deviner and essai_user != 0:
            try:
                nbr_taper = input('Taper un nombre entre 0 et 100: ')
                nbr_taper = int(nbr_taper)
                if nombre_a_deviner > nbr_taper:
                    print(f'Nombre a deviné est supérieur')
                    essai_user = essai_user - 1
                    print(f'Il vous reste {essai_user} essais')
                elif nombre_a_deviner < nbr_taper:
                    print(f'Nombre a deviné est inférieur')
                    essai_user = essai_user - 1
                    print(f'Il vous reste {essai_user} essais')
                else:
                    print(f'Bravo tu as trouvé')
                    victoir = True

                    break
            except ValueError:
                print("Veuillez réessayer")
                essai_user = essai_user - 1
                print(f'Il vous reste {essai_user} essais')
        print(f'Tour {tour} ,le nombre a deviné est: {nombre_a_deviner}')
        tour = tour - 1

        if victoir:
            tour_gagner = tour_gagner - 1
            print(f'Vous avez gagner\n')
        else:
            print(f'Vous avez perdu\n')

    if tour_gagner < 2:
        print(f'Gagner')
    else:
        print(f'Perdu')


if __name__ == '__main__':
    main()
