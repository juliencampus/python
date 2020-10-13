# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calMoyenne(dic):
    result = {sum(el) / len(el): name for name, el in dic.items()}

    return result[max(result)], round(max(result), 2)

def main():
    notes = {"Ulys": [0, 1, 3, 2], "Clément": [0, 10, 13, 15, 18, 20]}

    winner , avg = calMoyenne(notes)
    print("Le meilleur élève est ", winner, "avec la moyenne de", avg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
