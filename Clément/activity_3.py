import random

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

# variables
user1 = {'name' : 'Bernard', 'win': False, 'good_price': random.randint(0, 100)}
user2 = {'name' : 'Jean Claude', 'win': False, 'good_price': random.randint(0, 100)}
step = 0
print(f'{user1["name"]} doit deviner {user1["good_price"]}')
print(f'{user2["name"]} doit deviner {user2["good_price"]}')

# loop
while not user1['win'] and not user2['win'] and step < 5:
    step += 1
    user1['win'] = is_good_price(give_a_price(user1['name']), user1["good_price"])
    user2['win'] = is_good_price(give_a_price(user2['name']), user2["good_price"])

# result
if user1['win'] and not user2['win']:
    print(f'{user1["name"]} a gagné !')
elif user2['win'] and not user1['win']:
    print(f'{user2["name"]} a gagné !')
elif user1['win'] and user2['win']:
    print('Vous avez gagné tous les deux')
else:
    print('Vous avez perdu tous les deux')
