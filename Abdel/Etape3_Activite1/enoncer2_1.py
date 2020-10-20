import enoncer1_1


def pave_droit(largeur, longueur, hauteur):
    perimetre, aire = enoncer1_1.rectangle(largeur, longueur)
    volume = aire * hauteur
    return volume


dim_larg = input(f'Tape la dimention de la largeur: ')
dim_larg = int(dim_larg)
dim_long = input(f'Tape la dimention de la longueur: ')
dim_long = int(dim_long)
dim_haut = input(f'Tape la dimention de la hauteur: ')
dim_haut = int(dim_haut)
volume_pave = pave_droit(dim_larg, dim_long, dim_haut)
print(f'Le volume du pavé droit est : {volume_pave}')
