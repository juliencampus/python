chaine_etudiants = """213615200;BESNIER;JEAN
213565488;DUPOND;MARC
214665555;DURAND;JULIE"""

def string_to_dict(string):
    dict = {x.split(";")[0]: x.split(";")[1] + ' ' + x.split(";")[2] for x in string.split("\n")}
    return (dict)

print(string_to_dict(chaine_etudiants))


