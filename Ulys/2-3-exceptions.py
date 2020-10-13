import random
import time


class Player:

    def __init__(self,name):
        self.name = name
        self.guessed = False
        self.guess = int
        self.turn = 0
        self.data = []

    def play(self, target):
        t = time.time()
        result = "incorrect"
        try:
            self.guess = int(input(f'take a guess, {self.name}'))
        except ValueError:
            print('please enter a number')
            self.play(target)
        self.turn = self.turn + 1
        if self.guess < target:
            print('HIGHER !')
        elif self.guess > target:
            print('LOWER !')
        else:
            print(f' ! ! ! well done, {self.name} ! ! !')
            self.guessed = True
            result = "correct"
        self.data.append([self.turn, self.name, (time.time() - t), result])

    def total_time(self):
        time = 0
        for t in self.data:
            time += t[2]
        return time

    def avg_time(self):
        return self.total_time() / len(self.data)

    def time_to_string(self):
        return f'{self.name}\'s time : {self.total_time()}s (average {self.avg_time()}s / round)'


target = random.randint(0, 100)
cpt = 0
print('--Player 1--')
p1 = Player(input("What's your name baby ?"))
print('--Player 2--')
p2 = Player(input("What's your name baby ?"))

input('press ENTER when ready')

while cpt <= 5 or (not p1.guessed and not p2.guessed):

    print('---new round---')
    if not p1.guessed:
        p1.play(target)
    if not p2.guessed:
        p2.play(target)
    cpt = cpt+1

print('------------------')
if p1.guessed and p2.guessed:
    winner = p1 if p1.total_time() < p2.total_time() else p2
elif p1.guessed:
    winner = p1
elif p2.guessed:
    winner = p2
else:
    winner = "NOBODY"
print(f"""And th winner is...
....
...
*** {winner.name} ***!!
***********************""")

print(p1.time_to_string())
print(p2.time_to_string())

print(p1.data)
print(p2.data)




