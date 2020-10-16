def main():

    with open("nom.txt", 'r', encoding='utf-8') as nom_fichier:

        nom = nom_fichier.read()

        for row in nom:
            nom_auteur = row +" fait partie des meilleurs cinéastes de tout les temps"

            with open("auteur.txt", 'w', encoding='utf-8') as auteur_fichier:
                auteur_fichier.write(nom_auteur)

if __name__ == "__main__":
        main()
