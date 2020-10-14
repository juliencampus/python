import operator

dico = {}
dico ["Theo"] = 15
dico ["Clement"] = 35
dico ["Ulys"] = 42
dico ["Mlo"] = 16
dico ["Abdel"] = 72

    #--------------------tips--------------------------#

    # Afficher les valeurs des clef : dictionnaire.values()
    # Afficher la clef : dictionnaire.keys()
    # Afficher OrdreCroissant : Counter(Dictionnaire)


# Fonction calculer le total de vente :

def totalvente():
    compter = sum(dico.values())
    print(compter)
    # end


# Fonction qu'affiche le meilleur vendeur parmis un dicionnaire :

def meilleurvendeur():
    pseudo = dico.keys()
    bestvendeur = max(*sorted(enumerate(pseudo), key=operator.itemgetter(1)))
    print(f"Le meilleur vendeur est : {bestvendeur}")
    # end


# Fonction qui permet de transformer une chaine de caractère en dictionnaire (en gros) :

def numeroetudiant():
    chaine_etudiants = """213615200;BESNIER;JEAN
    213565488;DUPOND;MARC
    214665555;DURAND;JULIE"""
    print({str.split(";")[0]: str.split(";")[1] + str.split(";")[2] for str in chaine_etudiants.split("\n")})
    # end



# Fonction qui je sais pas encore trop à quoi elle va servir

def jesaispo():
    e = "Je crois ne pas avoir compris l'exercice demandé, a+"
    print(e)


jesaispo()
