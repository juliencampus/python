
class Player():

    def __init__(self, picNormally, picFight):
        self.picNormally = picNormally
        self.picFight = picFight
        self.x = 20
        self.y = 630
        self.life = 200
        self.width = 150
        self.height = 200
        self.isFight = False

    def fight(self, ennemi):
        self.isFight = True
        if(self.x + self.width - 20 > ennemi.x ):
            ennemi.life -= 10
            ennemi.x += 3

