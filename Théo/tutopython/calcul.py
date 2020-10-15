from math import pi
def calcul_aire_rect(longueur, largeur):
    aire = longueur * largeur
    perimetre = (longueur + largeur) * 2
    print("l'aire du rectangle est de", aire)
    print("le perimetre du rectangle est de", perimetre)
    return aire


calcul_aire_rect(10, 4)


def CircleArea(r):
    return pi * (r * r)


print("l'aire d'un cercle de rayon de 1 cm est " + str(CircleArea(1)) + "cm2")
print("l'aire d'un cercle de rayon de 5 cm est " + str(CircleArea(5)) + "cm2")
print("l'aire d'un cercle de rayon de 8 cm est " + str(CircleArea(8)) + "cm2")
print("l'aire d'un cercle de rayon de 10 cm est " + str(CircleArea(10)) + "cm2")


def perimetre_cercle(un_rayon):
    """Calculer le périmètre d'un cercle à partir de son rayon.
	:param un_rayon: le rayon du cercle (positif)
	:return le périmètre d'un cercle de rayon un_rayon
    """
    diametre = 2 * un_rayon
    return pi * diametre

def volume_pave(hauteur, longueur, largeur) :
    volume = (hauteur*longueur*largeur)
    print("le volume du pave est", volume)

volume_pave(2,4,5)

def volume_cylindre(rayon, hauteur) :
    volume = pi *(rayon*rayon)*hauteur
    print ("le volume du cylindre pour  hauteur", hauteur, "et un rayon de", rayon, "est de ", volume)

volume_cylindre(10, 4)


def main():
    """Le programme principal."""
    # demander le rayon à l'utilisateur
    saisie = input("Rayon du cercle : ")    # une chaîne de caractères
    le_rayon = float(saisie)                # convertie en un nombre réel

    # calculer le périmètre
    perimetre = perimetre_cercle(le_rayon)

    # afficher le périmètre à l'utilisateur
    print("Le périmètre d'un cercle de rayon", le_rayon, "est", perimetre)

if __name__ == "__main__":
    main()



def tri(mode) :
    liste = [7, 4, 10, 1, 24]
    print(sorted(liste, reverse = True if mode == "decroi" else False))




tri("decroi")

def testo() :
    word = "welephant"
    first = word[0]
    if first == "a" or first == "w" :
        print("trou")
    else :
        print("falz")


testo()




def initial(initial):
    dico = {"jean": "0610203040", "imotep": "0425784512", "aroun": "0615847455", "akiru": "0478965214"}
    return [x for i, x in dico.items() if i[0] == initial.lower()]
print(initial("a"))






def repertoire():
    dico = {
        "arf": 454808,
        "dzer": 447865
    }
    choix = 'z'
    while choix.lower() != 'q' :
        qsd = False
        while not qsd:
            choix = input(
            """ L pour lister
            A pour ajouter 
            S pour supprimer
            E pour envoyer vers le repertoire
            Q pour quitter""")
            try:
                choix = choix[0]
                qsd = True
            except ValueError:
                qsd = False
        print(choix)
        if choix == 'l':
            print(dico)
        elif choix == 'a':
            nouveau = input("ton blaz:")
            numero = False
            while not numero:
                try:
                    nouveaunum = int(input("le numero du bigo chef"))
                    numero = True
                except ValueError:
                    print("? t'est con ou quoi ? j'ai dit un numéro")
                    numero = False
            dico[nouveau] = nouveaunum
            print(f"bg, {nouveau} enregistrer")
        elif choix == 's':
            suppr = input("qui veut tu supprimer chef")
            if suppr in dico:
                print(f"ton pote {suppr}'à dégager")
                dico.pop(suppr)
            elif suppr.isdigit() and int(suppr) in list(dico.values()):
                key = list(dico.keys())[list(dico.values()).index(int(suppr))]
                print(f"le bogoss {key} n'existe plus ")
                dico.pop(key)
            else:
                print("n'existe pas")
        elif choix == "e":
            with open("repertoire.csv", "w") as fp:
                for k, v in dico.items():
                    fp.write(f"{k};{v}\n")
            print("envoyer vers le fichier repertoire")
        elif choix =="q":
            break

        else:
            print("mdr idiot !")


repertoire()