from Game import Game
from Character import *

g = Game()
p = Mage("théo")

g.place(0,0,p)
pp = Guerrier("oui")
g.place(0,1,pp)
print(g.teams)

