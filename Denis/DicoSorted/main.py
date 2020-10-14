# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def bestVendeur(dic):

    vente = 0

    for el, val in dic.items():
        if val > vente:
            vente = val
            vendeur = el

    return vendeur


def main():
    ventes={"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}

    print("Meilleur vendeur du jour :", bestVendeur(ventes))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
