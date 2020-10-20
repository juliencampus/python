import math


def cercle(rayon):
    perimetre = round(rayon * 2 * math.pi, 2)
    aire = round(rayon * rayon * math.pi, 2)
    return perimetre, aire


if __name__ == "__main__":
    dim = input(f'Tape la dimention du rayon: ')
    dim = int(dim)
    perimetre_cercle, aire_cercle = cercle(dim)

    print(f'Le périmètre du cercle est : {perimetre_cercle} et son aire est : {aire_cercle}')
