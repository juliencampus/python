

animaux2 = ["poisson", "abeille", "chat"]
with open("zoo2.txt", "w") as filout:
    for animal in animaux2:
        filout.write("{}\n".format(animal))

with open("zoo2.txt", "r") as filin:
    lignes = filin.readlines()
    for ligne in lignes:
        print(ligne)