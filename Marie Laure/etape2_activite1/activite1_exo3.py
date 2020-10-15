liste_1 = [13, 15, 12, 17, 15]
liste_2 = ["Fifi", "Riri", "Loulou"]
liste_3 = []

for i in range(len(liste_1)):
    if i < len(liste_1):
        liste_3.append(liste_1[i])
    if i < len(liste_2):
        liste_3.append(liste_2[i])

print(liste_3)


