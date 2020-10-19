from math import pi

def aire_peri_cercle():
    print("veuillez entrer le rayon du cercle: r =  ")
    r = float(input())
    s = pi*(r*r)
    print("Aire du cercle = ", s)


if __name__=="__main__":
    aire_peri_cercle()
