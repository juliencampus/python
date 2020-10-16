import itertools


def main():
    L1= [13, 15, 12, 17, 15]
    L2 = ["fifi", "riri", "loulou"]
    # sans itertools
    L3 = []
    for i in range(len(L1)):
        L3.append(L1[i])
        if i < len(L2):
            L3.append(L2[i])

    # compréhension de liste ==> itertools
    #result = [x for x in itertools.chain.from_iterable(itertools.zip_longest(L1, L2)) if x]

    print(L3)


if __name__ == "__main__":
    main()