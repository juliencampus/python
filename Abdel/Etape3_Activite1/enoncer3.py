def tri_liste(list_a_trier, ordre="crois"):
    item_liste = [item for item in list_a_trier]
    item_liste.sort(reverse=True if ordre == "decr" else False)
    list_a_trier = [item for item in item_liste]
    return list_a_trier


liste_a_trier = [25, 22, 58, 48, 94, 26, 99, 200, 589, 2]

print(f'Liste triée par ordre croissant : {tri_liste(liste_a_trier)}')

print(f'Liste triée par ordre décroissant : {tri_liste(liste_a_trier, "decr")}')