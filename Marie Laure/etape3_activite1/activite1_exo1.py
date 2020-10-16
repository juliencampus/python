import math


def rectangle(largeur, longueur):
    perimetre = (largeur + longueur) * 2
    aire = largeur * longueur
    return perimetre, aire


def cercle(rayon):
    perimetre = round(rayon * 2 * math.pi, 2)
    aire = round(rayon * rayon * math.pi, 2)
    return perimetre, aire


def pave_droit(largeur, longueur, hauteur):
    perimetre, aire = rectangle(largeur, longueur)
    volume = aire * hauteur
    return volume


def cylindre(rayon, hauteur):
    perimetre, aire = cercle(rayon)
    volume = aire * hauteur
    return volume


perimetre_rectangle, aire_rectangle = rectangle(5, 7)
perimetre_cercle, aire_cercle = cercle(3)
volume_pave = pave_droit(5, 7, 10)
volume_cylindre = cylindre(3, 10)

print(f'Le périmètre du rectangle est : { perimetre_rectangle } et son aire est : { aire_rectangle }')
print(f'Le périmètre du cercle est : { perimetre_cercle } et son aire est : { aire_cercle }')
print(f'Le volume du pavé droit est : { volume_pave }')
print(f'Le volume du cylindre droit est : { volume_cylindre }')

