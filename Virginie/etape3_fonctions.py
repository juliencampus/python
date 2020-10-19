import math

# En utilisant des fonctions

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


perimetre_rectangle, aire_rectangle = rectangle(12, 10)
perimetre_cercle, aire_cercle = cercle(9)
volume_pave = pave_droit(12, 6, 10)
volume_cylindre = cylindre(9, 10)

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


liste_a_trier = [25, 22, 58, 48, 94, 26, 99, 200, 589, 2]
# par defaut la liste est trieé par ordre croissant...
print(f'La liste triée par ordre croissant : { tri_liste(liste_a_trier) }')
# si non utiliser la méthode .sort (Pour trier des listes) avec une condition (paramètre reverse = booleen => si l'inverse est vrai)
print(f'La liste triée par ordre décroissant : { tri_liste(liste_a_trier, "decr") }')


# Fonction repertoire/phone ==> dictionnaire =  variable locale/globale

def phone_number(phone_directory, char="A"):
     find_number_A = [x + ' : ' + phone_directory[x] for x in phone_directory if x[0] == char]
     print(f'le num de tel commençant par la lettre A est : {find_number_A}')


directory = {'Claire': '0612345678', 'Maman': '0601020304', 'Mamie': '0709080706', 'Vivien': '0712326545', 'Angèle': '0102030405'}
phone_number(directory)

