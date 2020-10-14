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
    name = input('Saisir le nom du contact :\n')
    print(name.capitalize())
    number = input('Saisir le numero du contact :\n')
    my_dir[name] = number
    return 'contact ajouté'


def delete_in_directory(my_dir):
    print(list_directory(my_dir))
    name = input('quel contact voulez vous supprimer?')
    my_dir.pop(name)
    return 'contact supprimé'


# main program
while True:
    option = input('Choisir une option\n'
                   'L: Lister\n'
                   'A: Ajouter\n'
                   'D: Supprimer\n'
                   'Q: Quitter\n')

    if option.capitalize() == 'L':
        print(list_directory(directory))
    elif option.capitalize() == 'A':
        print(add_in_directory(directory))
    elif option.capitalize() == 'D':
        print(delete_in_directory(directory))
    elif option.capitalize() == 'Q':
        print('Fin du programme')
        break
    else:
        print(f'option{option} non valide')
