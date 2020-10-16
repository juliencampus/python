import random
import itertools as it

def un() :
    a=[]
    n=int(input("Enter number of elements:"))
    for i in range(n):
        a.append(random.randint(1,1000))
    tri = sorted(a)
    print(tri)


def trois() :
    a = [1, 2, 3, 4, 5]
    b = ["riri", "fifi", "loul",]
    c = [x for x in it.chain.from_iterable(it.zip_longest(a, b)) if x]
    print(c)

def un() :
    haystack = [1, 1, 15, 14, 15, 1, 2, 14, 0, 0]
    a = 15
    print(haystack.index(a)+haystack[haystack.index(a)+1:].index(a)+1)


def undeux() :
    liste = [13, 15, 12, 17, 15, 18, 15, 17]
    A = 17

    index_found = 0
    result = 1

    for i, element in enumerate(liste):
        if element == A:
            index_found += 1
            if index_found == 2:
                result = i
    print(result)

un()
undeux()
def quatre() :
    list1 = [1, 1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    L3 = [x for x in set(list1)] + [y for y in set(list2) if y not in list1]
    print(L3)
    ar = list(set(list1+list2))
    print (ar)


def cinque() :
    notes = [11, 17, 4, 20]
    coef = [2, 4, 1, 2]
    s=0
    sc=0
    for i in range(0,4):
       s = s+notes[i]*coef[i]
       sc = sc+coef[i]
    print(s/sc)
cinque()