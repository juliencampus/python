with open("monkeys.txt", "r") as fp:
    for row in fp.readlines():
        print(row.upper())

with open("monkeys.txt", "a") as rfp:
    m = input(">>new monkey ? :")
    rfp.write(f"\n{m}")
