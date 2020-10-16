def main():
    Val = [12.5, 13.6, 18.4, 9.7]
    Coeff = [2, 3, 5, 4]
    somme = 0

    for x, y in zip(Val, Coeff):
        somme += (x * y)
        resultat = somme / sum(Coeff)

    print(resultat)

if __name__ == '__main__':
    main()