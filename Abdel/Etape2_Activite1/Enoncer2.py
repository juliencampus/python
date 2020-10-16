import random


def main():

    liste = [random.randint(0, 100) for i in range(1000)]
    liste.sort()
    print(liste)

if __name__ == '__main__':
    main()