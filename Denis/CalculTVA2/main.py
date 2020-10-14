# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def askName():
    return input("Nom du produit ?")

def askTaxe():
    taxe = float(input("Taxe à mettre en place ?"))

    return round(taxe)

def askPrice():
    return float(input("Prix du produit ?"))

def askStock():
    return int(input("Stock du produit ?"))

def ttc(taxe, price):
    return (((taxe / 100) * price) + price)

def ttcStock(totalPrice, stock):
    return totalPrice * stock


def main():
    nameProduit = askName()
    priceProduit = askPrice()
    taxe = askTaxe()
    stock = askStock()
    totalPriceTaxe = ttc(taxe, priceProduit)
    totalPriceStock = ttcStock(totalPriceTaxe, stock)

    print("Le produit", nameProduit, " qui coute", priceProduit, "avec", taxe, "% de taxe, revient à", totalPriceTaxe, "€")

    if(totalPriceStock < 1000):
        print("Le total des produits en stock est de", totalPriceStock, "€")
    else:
        print("Le total des produits en stock est de", totalPriceStock, "€ avec 12% de remise soit", totalPriceStock - (totalPriceStock * float(12/100)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
