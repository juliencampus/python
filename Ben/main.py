import random

choixordi = random.randint(0, 100)
print(choixordi)
print("Tu as le droit à 10 chances !")

def devinequichui(lachance):

    while lachance != 0:
        lachance -= 1
        try:
            proposition = int(input("Quelle nombre penses-tu que j'ai choisi?"))
            if proposition < choixordi:
                print("Plus grand !")
                print("Il te reste :", lachance, "chance.")

            if proposition > choixordi:
                print("Plus petit ...")
                print("Il te reste :", lachance, "chance.")

            if proposition == choixordi:
                print("Bravo, tu as trouvé !")
                print("Il te restait :", lachance, "chance.")

            if lachance == 0:
                print("Dommage, tu as perdu !")

        except ValueError:
            print("Rentre un nombre stp")


devinequichui(10)