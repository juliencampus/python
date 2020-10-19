import characters
import itertools


class Game(object):
    def __init__(self):
        self._team_red = []
        self._team_blue = []

    def start_menu(self):
        print('Team Rouge ! Choisis tes combattants !!!')
        self.create_team(3)
        print('ton équipe est complète !\n\n\n\n')
        print('Team Bleu ! Choisis tes combattants !!!!!!!!!')
        self.create_team(3, False)
        print('\n')
        print('les équipes sont crées ! READY TO FIGHT !!!!!!!!!!!')
        print('\n')
        self.death_match()

    def create_team(self, nb, red=True):
        if red:
            team = self._team_red
            color = 'Rouge'
        else:
            team = self._team_blue
            color = 'Bleu'
        for i in range(nb):
            choice_is_made = False
            while choice_is_made == False :
                choice = input(f'Quel sera ton personnage n°{i+1}?\n'
                               f'1: Magicien\n'
                               f'2: Guerrier\n'
                               f'3: Archer\n')
                if choice == '1':
                    team.append((color, characters.Wizard(f'magicien {i+1}')))
                    print('tu as choisi un Magicien')
                    choice_is_made = True
                elif choice == '2':
                    team.append((color, characters.Warrior(f'guerrier {i+1}')))
                    print('tu as choisi un Guerrier')
                    choice_is_made = True
                elif choice == '3':
                    team.append((color, characters.Archer(f'archer {i+1}')))
                    print('tu as choisi un Archer')
                    choice_is_made = True
                else:
                    print('choix non valide')

    def fight_one_one(self, list1, list2):
        # Tour du premier joueur
        player = None
        # Selection du combattant
        for j1, e1 in enumerate(list1):
            if not e1[1].is_tired:
                player = e1[1]
                break
        if player is not None:
            print(f'Joueur {list1[0][0]}, votre {player.name} attaque !')
            print('quel ennemie est attaquer ?')

            # Options attaque premier Joueur
            fight_options = {}
            for j, e2 in enumerate(list2):
                print(f'{j}: Nom: {e2[1].name} | Santé:{e2[1].health} | Shield_magic: {e2[1].shield_magic} | shield_physic: {e2[1].shield_physic}')
                fight_options[j] = e2
            enemy = int(input())
            att_option = int(input('Quel type d\'attaque effetuer?\n'
                                   f'1 : Maqique {player.attack_magic}\n'
                                   f'2 : Physique {player.attack_physic}'))
            player.attack(list2[enemy][1], att_option)
            print(f'la santé du {list2[enemy][1].name} {list2[0][0]} est maintenant à {list2[enemy][1].health}')
            print('\n')
            if list2[enemy][1].health < 1:
                print(f'le{list2[enemy][1].name} est mort \n')
                list2.pop(enemy)

    def death_match(self):
        while len(self._team_red) > 0 and len(self._team_blue) > 0:
            print('\n\n')
            print('Equipe Rouge----------------------------------------------------')
            for i, v in enumerate(self._team_red):
                print(f'{self._team_red[i][1].name} Santé {self._team_red[i][1].health}')
            print('------------------------------------------------------------')
            print('Equipe Bleu-----------------------------------------------------')
            for i, v in enumerate(self._team_blue):
                print(f'{self._team_blue[i][1].name} Santé {self._team_blue[i][1].health}')
            print('------------------------------------------------------------')
            print('\n')
            # Remise à zero pour la manche
            for e in (self._team_blue + self._team_red):
                e[1].is_tired = False

            # Choix de la première équipe à jouer
            if len(self. _team_red) > len(self._team_blue):
                firstPLayerList = self._team_blue
                secondPLayerList = self._team_red
                longest_list = self._team_blue
            else:
                firstPLayerList = self._team_red
                secondPLayerList = self._team_blue
                longest_list = self._team_red

            for i in range(len(longest_list)):
                # Tour du premier joueur
                if i < len(firstPLayerList):
                    self.fight_one_one(firstPLayerList, secondPLayerList)

                # Tour second joueur
                if i < len(secondPLayerList):
                    self.fight_one_one(secondPLayerList, firstPLayerList)

        if len(self._team_red) == 0:
            print('------------------------------------------\n'
                  '----------LES BLEUX ONT GAGNES------------\n'
                  '------------------------------------------')
        else:
            print('------------------------------------------\n'
                  '----------LES ROUGES ONT GAGNES------------\n'
                  '------------------------------------------')


