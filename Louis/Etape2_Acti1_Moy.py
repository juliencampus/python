import random

def main():
    Nb_val = 100
    Val = []
    Coef = []
    somme_ValCoef = 0
    somme_Coef = 0

    for x in range(Nb_val):
        Val.append(round(random.uniform(1,20), 1))

    for x in range(Nb_val):
        Coef.append(random.randint(1, 5))

    for x in range(Nb_val):
        somme_ValCoef = somme_ValCoef + Val[x]*Coef[x]
        somme_Coef = somme_Coef + Coef[x]

    # print(Val)
    # print(Coef)
    print(round(somme_ValCoef / somme_Coef, 2))

if __name__ == "__main__":
    main()