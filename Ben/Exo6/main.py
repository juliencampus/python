def jesuislindex():
    L = [15, 17, 18, 24, 51, 51, 96]
    p = 0

    for i, e in enumerate(L):
        if e == 51:
            p += 1
            print(f"Le numéro {e} est présent à la position {i} pour la {p}èm fois")

jesuislindex()