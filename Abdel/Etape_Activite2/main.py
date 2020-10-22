def main():
    # Lecture dans un fichier .txt
    # with open("zoo.txt", "r") as filin:
    #     for ligne in filin:
    #         print(ligne)

    # Ecriture dans un fichier .txt
    # animaux = ["poi", "sson", "abei", "lle", "ch", "at"]
    # with open("zoo1.txt", "w") as filout:
    #     for animal in animaux:
    #         filout.write("{}\n".format(animal))

    # Ecriture dans un deuxieme fichier .txt en partant du premier fichier
    with open("zoo1.txt", "r") as fichier1, open("zoo2.txt", "w") as fichier2:
        for ligne in fichier1:
            fichier2.write("* " + ligne)


if __name__ == "__main__":
    main()
