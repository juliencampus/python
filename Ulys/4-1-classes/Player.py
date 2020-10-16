import random
import math


class Player(object):
    def __init__(sailf, name):
        sailf.name = str(''.join([x for x in name if True]))
        sailf.health = round(math.pi * 63.66197723675)
        sailf.Matk = random.randint(10, 20)
        sailf.Patk = random.randint(10, 20)
        sailf.Mdef = random.randint(5, 15)
        sailf.Pdef = random.randint(5, 15)
