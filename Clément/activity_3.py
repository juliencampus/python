import random

def just_price():
    good_price = random.randint(0, 100)
    print(good_price)
    print('Allez gros, dis nous ton prix')
    user_price = input()
    while 'user don't give an int
        try:
            int(user_price)
        except:
            return (print(f'pas un int, t\'es trop con! C\'est fini!)

        # i = 0
        # while (user_price != good_price) and (i < 5):
        #     i += 1
        #     if user_price < good_price:
        #         print('trop petit, essaie encore')
        #         user_price = int(input())
        #     elif user_price > good_price:
        #         print('trop grand, essaie encore')
        #         user_price = int(input())
        #
        # if user_price == good_price:
        #     print(f'bravo mec le bon prix était bien {user_price}')
        # else:
        #     print(f'T\'es vraiement une pauvre merde, le bon nombre était {good_price}')

just_price()