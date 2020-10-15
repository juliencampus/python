from Player import Player


class Weezard(Player):
    def __init__(thisParticularInstanceofAWeezard, name):
        Player.__init__(thisParticularInstanceofAWeezard,name)
        thisParticularInstanceofAWeezard.Matk *= 2
        thisParticularInstanceofAWeezard.Pdef *= .8


