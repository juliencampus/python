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


# print(liste.index(A))