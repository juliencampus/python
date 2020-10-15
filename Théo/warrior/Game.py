from Character import Character


class Game(object):
    TEAM_SIZE = 5
    def __init__(self):
        self.teams = [
            [0 for x in range(0, self.TEAM_SIZE)],
            [0 for x in range(0, self.TEAM_SIZE)]
        ]

    def place(self, team: int, position: int, player: Character):
        if team in range(0, 2) and position in range(0, self.TEAM_SIZE):
            if self.teams[team][position]:
                self.replace(team, position, player)
            else:
                self.teams[team][position] = player
        else:
            raise ValueError('team must be 1 or 2 and position between 0 - 4')

    def replace(self, team, position, player):
        choice = "a"
        while not (choice == "Y" or choice == "N"):
            choice = input(f"Would you like to replace {self.teams[team][position].nom} in team {team}, position {position} ?  Y/N")
            choice = choice.upper()
        if choice == "Y":
            self.teams[team][position] = player
