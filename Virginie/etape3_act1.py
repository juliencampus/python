from math import sqrt
from math import pi

# en utilisant des formules


def aire_peri_rect():


    print("Veuillez entrer le côté a : ")
    a = float(input())
    print("Veuillez entrer le côté b : ")
    b = float(input())
    print("Veuillez entrer le côté c : ")
    c = float(input())
    d = (a + b + c) / 2  # demi-périmètre
    s = sqrt(d * (d - a) * (d - b) * (d - c))  # aire (suivant formule)

    print("Longueur des côtés =", a, b, c)
    print("Périmètre =", d * 2, "Aire =", s)

if __name__ == "__main__":
    aire_peri_rect()


def aire_peri_cercle():
    print("veuillez entrer le rayon du cercle: r =  ")
    r = float(input())
    s = pi*(r*r)
    print("Aire du cercle = ", s)


if __name__=="__main__":
    aire_peri_cercle()