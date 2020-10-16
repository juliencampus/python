ventes = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}
def main():
    ventes = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}
    total_vente = 0

    for valeur in ventes.values():
        total_vente += valeur
    print(total_vente)
    return total_vente

if __name__ == '__main__':
    main()