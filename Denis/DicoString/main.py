# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def dicoMoi(chaine):

    return {item.split(';')[0]: item.split(';')[1] + item.split(';')[2] for item in chaine.split('\n')}

def main():
    chaine_etudiants = """213615200;BESNIER;JEAN
213565488;DUPOND;MARC
214665555;DURAND;JULIE"""

    print(dicoMoi(chaine_etudiants))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
