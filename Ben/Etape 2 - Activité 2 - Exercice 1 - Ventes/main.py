from collections import Counter
import operator

dico = {}
dico ["Theo"] = 15
dico ["Clement"] = 35
dico ["Ulys"] = 42
dico ["Mlo"] = 16
dico ["Abdel"] = 72

    # Afficher les valeurs des clef : dictionnaire.values()
    # Afficher la clef : dictionnaire.keys()
    # Afficher OrdreCroissant : Counter(Dictionnaire)

def totalvente():
    compter = sum(dico.values())
    print(compter)

def meilleurvendeur():
    pseudo = dico.keys()
    bestvendeur = max(*sorted(enumerate(pseudo), key=operator.itemgetter(1)))
    print(f"Le meilleur vendeur est : {bestvendeur}")


meilleurvendeur()
