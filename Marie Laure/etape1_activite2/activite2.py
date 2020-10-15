import random

tour = 0
set_won = 0

while tour < 3:
    random_number = random.randint(0, 100)
    attempt = 10

    while attempt > 0:
        user_guess = -1
        attempt -= 1
        while user_guess < 0 or user_guess > 100:
            user_guess = input("Choisissez un nombre entre 0 et 100.")
            try:
                user_guess = int(user_guess)
            except ValueError:
                print("Vous n'avez pas saisi un nombre")
                user_guess = -1
                continue
            if user_guess < 0:
                print("Vous ne pouvez pas saisir un nombre inférieur à 0.")
            if user_guess > 100:
                print("Vous ne pouvez pas saisir un nombre supérieur à 100.")

        if attempt == 10:
            print("Vous avez perdu.")
            print("************* Nouvelle manche *************")
            tour += 1
            break

        if random_number == user_guess:
            print("Félicitations ! Vous avez trouvé !")
            print("************* Nouvelle manche *************")
            set_won += 1
            tour += 1
            print(f'Manche { tour } / 3')
            break
        elif random_number < user_guess:
            print(f'C\'est trop grand. \nIl vous reste { attempt } tentatives.')
            continue
        else:
            print(f'C\'est trop petit. \nIl vous reste { attempt } tentatives.')
            continue

    if tour == 3:
        if set_won >= 2:
            print("C'est gagné !")
        else:
            print("C'est perdu.")