# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def melangeListes(liste1, liste2):

    liste = []

    for i in range(len(liste1) if len(liste1) > len(liste2) else len(liste2)):
        if(i < len(liste1)):
            liste.append(liste1[i])
        if(i < len(liste2)):
            liste.append(liste2[i])

    return liste


def main():
    liste1 = [10, 15, 20, 54, 68, 60, 64]
    liste2 = ["Abdel", "Théo", "Mlo", 'Ulys', "Louis", "Julien", "Camille", "Vivi"]

    liste = melangeListes(liste1, liste2)

    print(liste)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
