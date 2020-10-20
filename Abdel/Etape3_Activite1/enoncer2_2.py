import enoncer1_2


def cylindre(rayon, hauteur):
    perimetre, aire = enoncer1_2.cercle(rayon)
    volume = aire * hauteur
    return volume


dim_ra = input(f'Tape la dimention du rayon: ')
dim_ra = int(dim_ra)
dim_haut = input(f'Tape la dimention de la hauteur: ')
dim_haut = int(dim_haut)
volume_cylindre = cylindre(dim_ra, dim_haut)
print(f'Le volume du cylindre droit est : {volume_cylindre}')
