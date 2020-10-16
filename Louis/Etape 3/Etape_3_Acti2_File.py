import math

def main ():

    filin = open("zoo.txt", "r")
    file = filin.readlines()

    for el in file:
        print(el)

if __name__ == "__main__":
        main()