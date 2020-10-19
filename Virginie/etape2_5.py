import math


def main():

    val = [12.5, 13.6, 18.4, 9.7]
    coef = [2, 3, 5, 4]

    i = 0
    for x, y in zip(val, coef):
        i += x * y
    moyenne = i / sum(coef)

    print(f"La moyenne pondérée est de:{moyenne}")


if __name__ == "__main__":
    main()
