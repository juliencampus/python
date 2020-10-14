import math


# Activité 1:
def rectangle(length, height):
    area = length*height
    perimeter = length*2 + height*2
    return area, perimeter


def circle(r):
    area = round((r*r)*math.pi)
    perimeter = round(2*math.pi*r)
    return area, perimeter


def parallelepiped_volume(area, wide):
    return area * wide


def cylinder_volume(area, height):
    return area * height


# print(rectangle(25, 20))
# a1, p1 = rectangle(25, 20)
# print(circle(20))
# a2, p2 = circle(20)

# print(parallelepiped_volume(a1, 50))
# print(cylinder_volume(a2, 50))

def sort_list(li, rev=False):
    li.sort(reverse=rev)
    return li


# l1 = [5, 8, 6, 5, 2, 3]
# print(sort_list(l1, True))


def give_dict_value(my_dict, char):
    return [my_dict[e] for e in my_dict if e[0].capitalize() == char.capitalize()]


dict1 = {'Bernard': '0676587423', 'Berard': '0680557823', 'Micheline': '0780587823', 'Audrey': '0680558723', 'marceline': '0698588754'}
print(give_dict_value(dict1, 'm'))
