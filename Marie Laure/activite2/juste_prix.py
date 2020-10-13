import random

random_number = random.randint(0, 100)
attempt = 10
set = 3
play = True


while play:
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

    if random_number == user_guess:
        print("Félicitations ! Vous avez trouvé !")
        play = False
    elif random_number < user_guess:
        print("C'est trop grand. Il vous reste", attempt, "tentatives.")
        continue
    else:
        print("C'est trop petit. Il vous reste", attempt, "tentatives.")
        continue

    if attempt == 0:
        print("Vous avez perdu.")
