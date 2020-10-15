import random
import time


class Player:

    def __init__(self, name, life, set_won=0):
        self.name = name
        self.life = life
        self.set_won = set_won


def ask_user(max):
    while True:
        user_guess = input(f'Choisissez un nombre entre 0 et { max }.')
        try:
            user_guess = int(user_guess)
            return user_guess
        except ValueError:
            print("Vous n'avez pas saisi un nombre")
            user_guess = -1
        if user_guess < 0:
            print("Vous ne pouvez pas saisir un nombre inférieur à 0.")
        if user_guess > max:
            print(f'Vous ne pouvez pas saisir un nombre supérieur à { max }.')


def choose_level():
    levels = [50, 100, 1000]
    print("Level 1 : Trouver un numéro entre 0 et 50 \nLevel 2 : Trouver un numéro entre 0 et 100 \nLevel 3 : Trouver un numéro entre 0 et 1000")

    while True:
        level = input("Que choisis-tu ?")
        try:
            level = int(level)
            print(level)
            max = levels[level - 1]
            return max
        except ValueError:
            print("Mauvais choix Buddy")


def choose_name():
    name = input("Quel est ton nom ?")
    name = str(name)
    return name


def play_tour(player, max, lap, lap_data):
    time_begin = round(time.time())

    random_number = random.randint(0, max)
    attempt = 10
    win = False
    print(f'A toi de jouer { player.name } !')

    while attempt > 0:
        user_guess = ask_user(max)

        if user_guess == random_number:
            print("Félicitations ! Vous avez trouvé !")
            print("************* Nouvelle manche *************")
            player.set_won += 1
            time_end = round(time.time())
            win = True
            break

        elif user_guess > random_number:
            print(f'C\'est trop grand.')

        else:
            print(f'C\'est trop petit.')

        attempt -= 1
        print(f'Il te reste {attempt} essais')

    if not win:
        time_end = round(time.time())
        print("Vous avez perdu.")
        print("************* Nouvelle manche *************")

    time_lap = (time_end - time_begin)
    # update = {"Score": time_lap, "Player": player.name}
    lap_data[str(lap) + ':' + player.name] = {"Score": time_lap, "Player": player.name}


def main():
    # Choix des noms des personnages
    name_player1 = choose_name()
    player_1 = Player(name_player1, 5)
    name_player2 = choose_name()
    player_2 = Player(name_player2, 5)

    # Initialisation du dictionnaire qui stocke les données de chaque tour
    lap_data = {}
    lap = 1

    # Choix du niveau de difficulté
    max = choose_level()

    while lap <= 5:
        play_tour(player_1, max, lap, lap_data)
        play_tour(player_2, max, lap, lap_data)
        print(lap_data)
        lap += 1


if __name__ == '__main__':
    main()





