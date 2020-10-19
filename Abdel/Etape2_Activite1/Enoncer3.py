def main():
    liste_nbr = [13, 15, 12, 17, 15]
    liste_nom = ['Fifi', 'Riri', 'Loulou']
    liste_mel = []

    for i in range(len(liste_nbr)):
        liste_mel.append(liste_nbr[i])
        if i < len(liste_nom):
            liste_mel.append(liste_nom[i])

    print(liste_mel)

if __name__ == '__main__':
    main()