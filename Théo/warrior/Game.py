from Character import Character


class Game(object):
    def __init__(self):
        self.team1 = []
        self.team2 = []




    def place(self,team: int, position: int, player: Player):
        if team in range(0,2) and position in range(0,4):
            # correct values
        else:
            return  TypeError('')
