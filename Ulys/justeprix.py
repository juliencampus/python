import random
won = 0


def ask():
    try:
        guess = int(input('take a guess:'))
    except ValueError:
        print('please enter a number')
        ask()
    return guess


for i in [0, 3]:
    target = random.randint(0, 100)
    cpt = 0
    guess = 101
    print('---new round---')
    while guess != target and cpt <= 10:
        guess = ask()
        cpt = cpt+1
        if guess < target:
            print('higher! ')
        elif guess > target:
            print('lower !')
        else:
            print('well done')
            won = won+1

print(f"won {won}/3")
