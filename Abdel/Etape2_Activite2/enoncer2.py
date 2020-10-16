def main():

    d_ventes = {"Dupont": 85, "Hervy": 39, "Geoffroy": 85, "Layec": 21}
    vendeur_num_1 = max(d_ventes, key=d_ventes.get)
    print(f'Vendeur n°1 est: {vendeur_num_1}')

if __name__ == '__main__':
    main()


