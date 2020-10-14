import math

ventes={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21, "biggest":21}

print((lambda l : sum(l.values()))(ventes)) #1

print((lambda l : max(l.items())[0] )(ventes)) #2

chaine_etudiants = """213615200;BESNIER;JEAN
213565488;DUPOND;MARC
214665555;DURAND;JULIE"""

print({str.split(";")[0]: str.split(";")[1] + str.split(";")[2] for str in chaine_etudiants.split("\n")}) #3

