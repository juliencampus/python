def main():
    ma_liste = [13, 15, 12, 17, 15, 18, 15, 17]
    nbrTaper = input('Taper un nombre: ')
    nbrTaper = int(nbrTaper)

    if nbrTaper in ma_liste:
        id1_list = ma_liste.index(nbrTaper)
        try:
            id2_list = ma_liste[id1_list + 1:].index(nbrTaper) + 1
            id_val2_repeter = id1_list + id2_list
            print(f"Le deuxiéme {nbrTaper} se trouve à l'index {id_val2_repeter}.")
        except:
            print(f"Le {nbrTaper} se trouve à l'index {id1_list}.")
    else:
        print(f"Le {nbrTaper} ne se trouve pas dans l'index.")


if __name__ == '__main__':
    main()
