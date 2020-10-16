import math

def main ():

    # ---- Functions

    def rectangle(largeur, longueur):
        perimetre = (largeur + longueur) * 2
        aire = largeur * longueur
        return perimetre, aire

    def cercle(rayon):
        perimetre = round(2 * math.pi * rayon, 2)
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


    # ---- Globals Variables

    perimetre_rectangle, aire_rectangle = rectangle(5, 2)
    perimetre_cercle, aire_cercle = cercle(10)
    volume_pave = pave_droit(5, 7, 10)
    volume_cylindre = cylindre(3, 10)

    # ---- Program

    print(f'Le périmètre du rectangle est : { perimetre_rectangle } et son aire est : { aire_rectangle }')
    print(f'Le périmètre du rectangle est : { perimetre_cercle } et son aire est : { aire_cercle }')
    print(f'Le volume du pavé droit est : {volume_pave}')
    print(f'Le volume du cylindre droit est : {volume_cylindre}')

    # Fonction de tri par ordre croissant ou décroissant

    # def sort_list(li, rev=False):
    #     li.sort(reverse=rev)
    #     return li
    #
    # l1 = [5, 8, 6, 5, 2, 3]
    # print(sort_list(l1, True))


    def tier_liste(liste, tri=False):
        liste.sort(reverse=tri)
        return liste

    liste = [5, 8, 6, 8, 9, 1, 3, 7, 5, 3]
    print(tier_liste(liste, True))


    def give_dict_value(my_dict, char):
        return [my_dict[e] for e in my_dict if e[0].capitalize() == char.capitalize()]

    dict1 = {'Bernard': '0676587423', 'Berard': '0680557823', 'Micheline': '0780587823', 'Audrey': '0680558723',
             'marceline': '0698588754'}
    print(give_dict_value(dict1, 'm'))

    dict_tel_nom = {'Bernard': '0676587423', 'Berard': '0680557823', 'Micheline': '0780587823', 'Audrey': '0680558723',
                     'marceline': '0698588754'}


if __name__ == "__main__":
        main()