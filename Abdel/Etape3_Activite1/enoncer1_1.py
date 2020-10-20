def rectangle(largeur, longueur):
    perimetre = (largeur + longueur) * 2
    aire = largeur * longueur
    return perimetre, aire


if __name__ == "__main__":
    dim_larg = input(f'Tape la dimention de la largeur: ')
    dim_larg = int(dim_larg)
    dim_long = input(f'Tape la dimention de la longueur: ')
    dim_long = int(dim_long)
    perimetre_rectangle, aire_rectangle = rectangle(dim_larg, dim_long)

    print(f'Le périmètre du rectangle est : {perimetre_rectangle} et son aire est : {aire_rectangle}')
