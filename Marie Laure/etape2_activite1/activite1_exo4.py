liste_1 = [13, 15, 12, 17, 15]
liste_2 = [18, 15, 14, 13, 19, 20]
liste_3 = []


# Méthode classique pour concaténer deux listes sans doublon

# for i in liste_1:
#     if i not in liste_3:
#         liste_3.append(i)
#
# for j in liste_2:
#     if j not in liste_3:
#         liste_3.append(j)


# Méthode avec la compréhension de listes

[liste_3.append(i) for i in liste_1 if i not in liste_3]
[liste_3.append(j) for j in liste_2 if j not in liste_3]

print(liste_3)