
# EXO POUR CREER UN FICHIER BINAIRE

def binaire():
    r = input(f'Entre le nom de ton fichier :')
    r = open(f"{r}.bin", "w")
    print(r)
    r.close()
