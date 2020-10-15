import requests


# variables
directory = {'BERNARD': '0676587423',
             'GERARD': '0680557823',
             'MICHELINE': '0780587823',
             'AUDREY': '0680558723',
             'MARCELINE': '0698588754',
             'BARNABE': '0698588754'}


# functions
def list_directory(my_dir):
    return sorted([e+': '+my_dir[e] for e in my_dir])


def add_in_directory(my_dir):
    name = input('Saisir le nom du contact :\n').upper()
    number = input('Saisir le numero du contact :\n')
    my_dir[name] = number
    return 'contact ajouté'


def delete_in_directory(my_dir):
    print(list_directory(my_dir))
    name = input('quel contact voulez vous supprimer?\n')
    while True:
        try:
            my_dir.pop(name.upper())
        except:
            print(f'{name} n\'est pas dans la liste')
            print(list_directory(my_dir))
            name = input('quel contact voulez vous supprimer?\n')
        else:
            break
    return 'contact supprimé'


def save_directory(my_dir):
    with open("my_text_file.txt", "w") as fic:
        for k in my_dir:
            fic.write(k +': '+my_dir[k]+'\n')
        fic.close()
    return print("répertoire enregistré")


def scrap_img_url(url):
    return requests.get(url).text.count("<img")

# main program
while True:
    option = input('Choisir une option\n'
                   'L: Lister\n'
                   'A: Ajouter\n'
                   'D: Supprimer\n'
                   'S: Save\n'
                   'I: Récupérer les images d\'un site web\n'
                   'Q: Quitter\n').upper()

    if option == 'L':
        print(list_directory(directory))
    elif option == 'A':
        print(add_in_directory(directory))
    elif option == 'D':
        print(delete_in_directory(directory))
    elif option == 'S':
        print(save_directory(directory))
    elif option == 'I':
        print(scrap_img_url('https://le-campus-numerique.fr/'))
    elif option == 'Q':
        print('Fin du programme')
        break
    else:
        print(f'option{option} non valide')


