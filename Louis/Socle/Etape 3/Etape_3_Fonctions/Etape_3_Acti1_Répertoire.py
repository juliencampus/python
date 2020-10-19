from pip._vendor import requests

phone_directory = {'Ben': '0102030405',
                   'Théo': '0201030405',
                   'Clem': '0345658798',
                   'Vivi': '0765854598',
                   'Abdel': '0645874125',
                   'Louis': '0678985465',
                   'Dni': '0574859677',
                   'Ulys': '0645857412'}

def main(phone_directory):



    def list_directory(phone_directory):
        return sorted([x + ' : ' + phone_directory[x] for x in phone_directory])

    def add_contact(phone_directory):
        while True:
            name = input('Saisis le nom du contact :\n')
            phone_number = input('Saisis le numéro du contact : \n')
            try:
                name = str(name).capitalize()
                phone_number = str(phone_number)
                phone_directory[name] = phone_number
                print('Le contact a été ajouté.')
                return ''
            except ValueError:
                print('Saisis un numéro, banane !')

    def delete_contact(phone_directory):
        print(list_directory(phone_directory))
        name = input('Tapes le nom du contact à supprimer :\n')
        while True:
            try:
                phone_directory.pop(name.capitalize())
                print('Le contact a été supprimé.')
                return ''
            except KeyError:
                print(f'Le contact {name} n\'existe pas, petit malin ...')
                continue

    def save_directory(phone_directory):
        with open("mon_repertoire.txt", "w") as file:
            for contact in phone_directory:
                file.write(contact + ':' + phone_directory[contact] + '\n')
            file.close()
        print('Le répertoire a bien été sauvegardé.')
        return ''

    def scrap_images():
        url = input('Saisis une url valide ...')
        url = str(url)
        return requests.get(url).text.count("<img")

    def choice_user():
        while True:
            choice = input('Choisir une option :\n'
                           'L : Lister les contacts \n'
                           'A : Ajouter un contact\n'
                           'D : Supprimer un contact\n'
                           'S : Sauvegarder le répertoire\n'
                           'I : Compter le nb d\'images sur un site web (avoues que tu t\'ennuies ...) -_-\n'
                           'Q : Quitter')
            try:
                choice = str(choice).upper()
                return choice
            except ValueError:
                print("Fais le malin !")

    while True:
        choice = choice_user().capitalize()
        if choice == 'L':
            print(list_directory(phone_directory))
            continue
        elif choice == 'A':
            print(add_contact(phone_directory))
            continue
        elif choice == 'D':
            print(delete_contact(phone_directory))
            continue
        elif choice == 'S':
            save_directory(phone_directory)
            continue
        elif choice == 'I':
            print(scrap_images())
            continue
        elif choice == 'Q':
            print("Ciao !")
            break
        else:
            print('Haha, très drôle, apprends à lire ...')
            choice_user()

if __name__ == "__main__":
        main(phone_directory)