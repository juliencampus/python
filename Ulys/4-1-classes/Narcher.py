from Player import Player

#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
class Narcher(Player):                    #♥
    def __init__(notme, name):            #♥
        Player.__init__(notme, name)      #♥
        notme.health *= 1.2               #♥
        notme.Mdef *= .8                  #♥
        notme.Pdef *= .8                  #♥
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
