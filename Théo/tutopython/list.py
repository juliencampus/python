import random
a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(random.randint(1,1000))
tri = sorted(a)
print(tri)