
# EXO POUR CREER UN FICHIER BINAIRE
# EXO POUR CREER UN FICHIER TXT

# ------------ PLEASE START IN MAIN.PY --------------- #


def binaire():
    b = input(f'Entre le nom de ton fichier :')
    b = open(f"{b}.bin", "w")
    print(b)
    b.close()

def txt():
    t = input(f'Entre le nom de ton fichier :')
    t = open(f"{t}.txt", "w")
    print(t)
    t.close()


def start():
    choixExo = int(input("TAPE 1 POUR CREER UN FICHIER TXT \n"
                     "TAPE 2 POUR CREER UN FICHIER BIN\n : "))
    if choixExo == 1:
        print("jesuisdansleif txt")
        txt()
    if choixExo == 2:
        binaire()