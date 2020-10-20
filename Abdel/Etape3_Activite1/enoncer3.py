def tri_liste(liste_a_trier, ordre="crois"):
    item_liste = [item for item in liste_a_trier]
    item_liste.sort(reverse=True if ordre == "decr" else False)
    liste_a_trier = [item for item in item_liste]
    return liste_a_trier


liste_a_trier = [25, 22, 58, 48, 94, 26, 99, 200, 589, 2]
# par defaut la liste est trieé par ordre croissant...
print(f'La liste triée par ordre croissant : {tri_liste(liste_a_trier)}')
# si non utiliser la méthode .sort (trier) avec une condition (si l'inverse est vrai)
print(f'La liste triée par ordre décroissant : {tri_liste(liste_a_trier, "decr")}')