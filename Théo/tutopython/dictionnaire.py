import operator
ventes = {}
ventes["dupont"] = 14
ventes["zlatan"] = 4
ventes["zemmour"] = 15
ventes["louis"] = 201
b = max(ventes.items(), key=operator.itemgetter(1))[0]
h = max(ventes, key=ventes.get)
a = sum(ventes.values())
print("il y a", a, "ventes au total")
print(b)
print(h)


chaine_etudiants = """213615200;BESNIER;JEAN
213565488;DUPOND;MARC
214665555;DURAND;JULIE"""
print({str.split(";")[0] : str.split(";")[1] + str.split(";")[2] for str in chaine_etudiants.split("\n") })