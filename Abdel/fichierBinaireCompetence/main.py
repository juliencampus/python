def main():
    # Ecriture dans un fichier .bin
    # animaux = ["poi", "sson", "abei", "lle", "ch", "at"]
    # with open("zoo1.bin", "w") as filout:
    #     for animal in animaux:
    #         filout.write("{}\n".format(animal))

    ["sson", "abei", "lle", "ch", "at", "image.png"]
    with open("zoo1.bin", "rb") as filout:
        for animal in filout:
            print(animal)


if __name__ == "__main__":
    main()
