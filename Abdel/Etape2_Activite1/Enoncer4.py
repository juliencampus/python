def main():
    liste_1 = [13, 15, 12, 17, 15]
    liste_2 = [18, 15, 14, 13, 19, 20]
    liste_3 = liste_1 + liste_2

    new_list = []
    for i in liste_3:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

if __name__ == '__main__':
    main()