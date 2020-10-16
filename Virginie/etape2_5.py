import math


def main():
    val = [12.5, 13.6, 18.4, 9.7]
    coef = [2, 3, 5, 4]
    val_coeff = [val * coef[i] for i, note in enumerate(val)]
    moy_ponderee = round((sum(val_coeff) / sum(coef)), 2)

    print(f"La moyenne pondérée est de:{moy_ponderee}")



if __name__ == "__main__":
    main()
