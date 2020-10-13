import random
import itertools as it
import time
s=time.time()
def premier():
    haystack = [1, 1, 15, 14, 14, 15, 1, 2, 0 ,0]
    needle = 14
    print(haystack.index(needle))

def second():
    print(sorted([random.randint(0,1000) for i in range(int(input("Enter number of elements:")))]))

def troisieme():
    a=['foo','bar','fun']
    b=[1,15,159,1598,2]
    print([x for x in it.chain.from_iterable(it.zip_longest(a, b)) if x])

def quatrieme():
    L1 = [13, 15, 12, 17, 15]
    L2 = [18, 15, 14, 13, 19, 20, 20]
    L3 = [x for x in set(L1)] + [y for y in set(L2) if y not in L1]
    print(L3)

def cinquieme():
    Val = [12.5, 13.6, 18.4, 9.7]
    Coeff = [2, 3, 5, 4]
    _sum = 0
    for i,x in enumerate(Val):
        _sum = _sum + x*Coeff[i]
    avg = _sum/float(sum(Coeff))
    print(avg)


#premier()
#second()
#troisieme()
#uatrieme()
#cinquieme()

print(time.time()-s)