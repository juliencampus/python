import random
import time

# functions
def give_a_price(user):
    user_price = input(f'Allez {user}, dis nous ton prix \n')
    while 'user don\'t give an int':
        try:
            int(user_price)
        except:
            user_price = input(f'Not an int, please {user} give me an int \n')
        else:
            user_price = int(user_price);
            break
    return user_price


def is_good_price(u_price, g_price):
    res = False
    if u_price < g_price:
        print('trop petit!')
        return res
    elif u_price > g_price:
        print('trop grand!')
        return res
    else:
        print('Bravo c\'est ok pour toi !')
        res = True
    return res

def is_good_price(u_price, g_price):
    res = False
    if u_price < g_price:
        print('trop petit!')
        return res
    elif u_price > g_price:
        print('trop grand!')
        return res
    else:
        print('Bravo c\'est ok pour toi !')
        res = True
    return res

def real_price(option):
    if option == '2':
        return random.randint(0, 100)
        print('Niveau Moyen')
    elif option == '3':
        return random.randint(0, 1000)
        print('Niveau Difficile')
    else:
        return random.randint(0, 50)




# variables
users = {1: {'total_time': 0, 'score': 0},
         2: {'total_time': 0, 'score': 0}}
# naming players
users[1]['name'] = input('joueur inconnu, donne moi ton nom\n')
print(f'Bonjour {users[1]["name"]}')
users[2]['name'] = input('joueur inconnu, donne moi ton nom\n')
print(f'Bonjour {users[2]["name"]}')

# choosing difficulty
diff_choice = -1
while diff_choice == -1:
    diff_choice = input(f'Quel niveau dfiificulté?\n1:Facile\n2:Moyen\n3:Difficile\n')
    if diff_choice == '1':
        print('Niveau Facile')
    elif diff_choice == '2':
        print('Niveau Moyen')
    elif diff_choice == '3':
        print('Niveau Difficile')
    else:
        print(f'la valeur{diff_choice} n\'est pas une option valide')

game_set = 0
while game_set < 3 and abs(users[1]['score']-users[2]['score']) < 2:

    good_price = real_price(diff_choice)
    print(f' prix a deviner {good_price}')
    game_set += 1
    for user in users:
        users[user]['win'] = False
    print(f'Manche numero {game_set}')
    if random.randint(1, 2) == 1:
        player1 = users[1]
        player2 = users[2]
    else:
        player1 = users[2]
        player2 = users[1]
    print(f'{player1["name"]} est le premier Joueur')
    step = 0
    # loop
    while not player1['win'] and not player2['win'] and step < 5:
        step += 1
        time_start = round(time.time())
        player1['win'] = is_good_price(give_a_price(player1['name']), good_price)
        player1['total_time'] += time.time() - time_start
        if not player1['win']:
            time_start = round(time.time())
            player2['win'] = is_good_price(give_a_price(player2['name']), good_price)
            player2['total_time'] += time.time() - time_start
    # result
    if player1['win'] and not player2['win']:
        print(f'{player1["name"]} a gagné la manche!')
        player1["score"] += 1
    elif player2['win'] and not player1['win']:
        print(f'{player2["name"]} a gagné la manche!')
        player2["score"] += 1
    elif player1['win'] and player2['win']:
        print('Vous avez  tous les deux gagné cette manche')
        player1["score"] += 1
        player2["score"] += 1
    else:
        print('Vous avez tous les deux perdu cette manche')
    print(users)
print(f'Partie terminée en {game_set} manches')

