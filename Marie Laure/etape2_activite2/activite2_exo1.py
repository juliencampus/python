ventes = {"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}

def total_ventes(ventes):
    total = 0
    for vente in ventes.values():
        total += vente
    return total

print(f'Le nombre total de ventes est : {total_ventes(ventes)}')