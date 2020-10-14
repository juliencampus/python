import random

list_random = []

i = 0
while i < 1000:
    list_random.append(random.randint(0, 1000))
    i += 1

print(list_random)
list_random.sort()
print(list_random)





