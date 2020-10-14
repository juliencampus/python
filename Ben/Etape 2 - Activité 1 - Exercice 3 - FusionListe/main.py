import itertools as it

def main():
    liste_entier = [1, 2 ,3 ,4 ,5]
    liste_character = ["Ulys", "Abdel", "Mlo", "Clem", "desolepourlesautrejailaflemmedemettretlm"]
    ma_liste = [ x for x in it.chain.from_iterable(it.zip_longest(liste_entier, liste_character)) if x]
    print(ma_liste)

main()