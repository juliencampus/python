sales = {"Dupont" : 14, "Hervy" : 19, "Geoffroy" : 15, "Layec" : 21, "Donald" :
    21}


def total_sales(sales):
    total = 0
    for sale in sales.values():
        total += sale
    return total


print(f'Le nombre total de ventes est : {total_sales(sales)}')


def employee_of_the_month(sales):
    best_sale = 0
    best_seller = 0
    for seller, sale in sales.items():
        if sale > best_sale:
            best_sale = sale
            best_seller = seller
    return best_seller

print(f'Le meilleur vendeur est : {employee_of_the_month(sales)}')


