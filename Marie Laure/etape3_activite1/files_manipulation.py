import requests
import os
import shutil

def main():
    # Chemin du répertoire à créer
    path = os.getcwd() + "\\test"
    os.mkdir(path)

    # Récupération de l'image
    response = requests.get("https://i.pinimg.com/originals/72/34/4b/72344b0b2bae63a79cedc96ac173ef4b.jpg")

    # Crée un fichier à écrire en mode binaire.
    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

    # Chemin source de l'image
    source = os.getcwd() + "\sample_image.png"

    # Chemin de destination de l'image
    destination = path + "\sample_image.png"

    # Déplacement de l'image dans le répertoire créé
    shutil.move(source, destination)

if __name__ == "__main__":
    main()