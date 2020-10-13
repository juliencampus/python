import random

def premier():
    haystack = [1, 1, 15, 14, 14, 15, 1, 2, 0 ,0]
    needle = 14
    print(haystack.index(needle))

def second():
    print(sorted([random.randint(0,1000) for i in range(int(input("Enter number of elements:")))]))

premier()
#second()
