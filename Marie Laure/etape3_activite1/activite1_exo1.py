import math

# Fonctions de calcul de périmètre, aire et volume

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


# Fonction de tri par ordre croissant ou décroissant

def tri_liste(liste_a_trier, ordre="crois"):
    item_liste = [item for item in liste_a_trier]
    item_liste.sort(reverse=True if ordre == "decr" else False)
    liste_a_trier = [item for item in item_liste]
    return liste_a_trier


liste_a_trier = [14, 22, 58, 67, 94, 26, 32]
print(f'La liste triée par ordre croissant : { tri_liste(liste_a_trier) }')
print(f'La liste triée par ordre décroissant : { tri_liste(liste_a_trier, "decr") }')




