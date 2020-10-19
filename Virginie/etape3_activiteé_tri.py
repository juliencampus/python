#lire un fichier
with open("zoo.txt", 'r') as filin:
   lignes = filin.readlines()
   for ligne in lignes:
       print(ligne)
#
#ecrire dans un fichier / on crée le fichier en même temps
animaux2 = ["poisson", "punaise", "abeille", "morue", "lemurien", "cochon", "chat", "migale", "tonton", "tata", "truite", "serpent"]

with open("zoo2.txt", "w") as filout:
    for animal in animaux2:
        filout.write("{}\n".format(animal))

# ouvrir deux fichiers en même temps
with open("zoo.txt", "r") as fichier1, open("zoo3.txt", "w") as fichier2:
    for ligne in fichier1:
        fichier2.write("* " + ligne)