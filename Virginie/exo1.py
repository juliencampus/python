import math


def produits_ttc(prixht, taxe, stock):
    prixtotalttc = (stock * (prixht + (prixht * taxe) / 100))
    return prixtotalttc


def remise(prixtotalttc, reduc):
    return prixtotalttc - (prixtotalttc * reduc)


def main():
    """Le programme principal."""
    # demander le produit, la quantité, le prix ht et la taxe, à l'utilisateur
    nom_produit = input("Nom du produit : ")  # une chaîne de caractères
    stock = input("quantité de produit ?")
    prixht = input("prixht :")
    taxe = input("TVA : ")

    # convertie en un nombre réel
    nom_produit = str(nom_produit)
    stock = float(stock)
    prixht = float(prixht)
    taxe = float(taxe)
    reduc = 0.12

    taxe = math.ceil(taxe)
    if taxe % 2 != 0:
        taxe = taxe + 1

    prixtotalttc = produits_ttc(prixht, taxe, stock)

    if prixtotalttc >= 1000:
        prixtotalttc = remise(prixtotalttc, reduc)
        print(
            f"Le total TTC du stock de  {nom_produit} est de prixttc {prixtotalttc} € (taxe de {taxe}% avec une remise de {reduc})")
    else:
        print(f"Le total TTC du stock de  {nom_produit} est de prixttc {prixtotalttc} € (taxe de {taxe} %)")

if __name__ == "__main__":
        main()


# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
