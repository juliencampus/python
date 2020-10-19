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



    def tier_liste(liste, tri=False):
        liste.sort(reverse=tri)
        return liste

    liste = [5, 8, 6, 8, 9, 1, 3, 7, 5, 3]
    print(tier_liste(liste, True))

    # Fonction de correspondance dans un dictionnaire

    def finding_nemo(phone_directory, char="A"):
        print([x + ' : ' + phone_directory[x] for x in phone_directory if x[0] == char])

    directory = {'Clément': '0612345678', 'Ulys': '0601020304', 'Denis': '0709080706', 'Vivi': '0712326545',
                 'Amélie': '0102030405', 'Dni': '0563254178'}
    finding_nemo(directory, "D")


if __name__ == "__main__":
        main()