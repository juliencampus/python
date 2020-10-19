import random

def main():

    # list_int_1 = []
    # list_int_1.append(random.randint(1, 100))
    #
    # list_int_2 = []
    # list_int_2.append(random.randint(1, 100))
    #
    # print(list_int_1)
    # print(list_int_2)
    #
    # list_int_1.extend(list_int_2)
    # print(list_int_1)

    list_int_1 = list(range(1, 21))
    list_int_2 = list(range(8, 33))

    print(list_int_1)
    print(list_int_2)

    # for x in list_int_2:
    #     if x not in list_int_1:
    #        list_int_1.append(x)

    list_int_1.extend(x for x in list_int_2 if x not in list_int_1)
    print(list_int_1)


if __name__ == "__main__":
    main()