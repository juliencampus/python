import math
import random
import itertools


# Etape1
# Activité 1
def taxe():
    print(f'Hi, say my name')  # Press Ctrl+F8 to toggle the breakpoint.
    name = input()
    print(f'Hi, say my price')
    price = float(input())
    print(f'Hi, say my taxe')
    rate = input()
    rate = math.ceil(float(input()))
    print(f'Ok,  taxe is {rate}%')
    ttc_price = price - (price*rate/100)
    print(f'le prix TTC du produit {name} est de {ttc_price} euros')
    print(f'Hi, how many {name} in your stock ?')
    stock = int(input())
    if stock * ttc_price < 1000:
        print(f'le stock TTC du produit {name} est de {ttc_price} euros')
    else:
        print(f' avec la remise de 12% le prix total est de {stock*ttc_price - stock*ttc_price*12/100}')


# Activité 2
def just_price():
    good_price = random.randint(0, 100)
    print(good_price)
    print('Allez gros, dis nous ton prix')
    user_price = int(input())
    i = 0
    while (user_price != good_price) and (i < 5):
        i += 1
        if user_price < good_price:
            print('trop petit, essaie encore')
            user_price = int(input())
        elif user_price > good_price:
            print('trop grand, essaie encore')
            user_price = int(input())

    if user_price == good_price:
        print(f'bravo mec le bon prix était bien {user_price}')
    else:
        print(f'T\'es vraiement une pauvre merde, le bon nombre était {good_price}')


# Etape 2
# Activité 1
def lists_and_tuples(my_list, my_value):
    is_in_list = False
    nb_in_list = 0
    for i, el in enumerate(my_list):
        if el == my_value:
            nb_in_list += 1
            if nb_in_list < 3:
                is_in_list = True
                good_index = i
                print(f'la valeur {my_value} n° {nb_in_list} est à la position {good_index}')
    if is_in_list:
        return good_index
    else:
        return print(f'le nb {my_value} n\'est pas dans la list')


def list_generator(nb_max, list_size):
    oh_my_list = sorted([random.randint(0, nb_max) for i in range(list_size)])
    return oh_my_list, oh_my_list[random.randint(0, list_size-1)]


# list1, value1 = list_generator(10, 10)
# lists_and_tuples(list1, value1)

def list_mix(l1, l2):
    result_list1 = [x for sublist in itertools.zip_longest(l1, l2) for x in sublist if x is not None]
    return result_list1

# list1 = [13, 15, 12, 17, 15]
# list2 = ["Fifi", "Riri", "Loulou"]
# list_mix(list1, list2)


def list_concat(l1, l2):
    result_list =[i for index, i in enumerate(l1+l2) if i not in (l1+l2)[:index]]
    print(result_list)


# list1 = [13, 15, 12, 17, 15]
# list2 = [16, 18, 12, 17, 22]
# list_concat(list1, list2)

def list_average(vlist, clist):
    result = sum([i*c for i, c in zip(vlist, clist)])/sum(clist)
    print(result)

# val = [12.5, 13.6, 18.4, 9.7]
# coeff = [2, 3, 5, 4]
# list_average(val, coeff)

# Activité 2
def total_sales(dict):
    total = 0
    for e in dict:
        total += dict[e]
    print(total)
    return (total)


# sales = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}
# total_sales(sales)

def best_saler(dict):
    return max(dict)

# sales = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}
# print(best_saler(sales))


def students_serial(string):
    result = {}
    for e in string.split('\n'):
        s = e.split(";")
        result.update({s[0]: s[1]+' '+s[2]})
    print(result)
    return result


# string_students = "213615200;BESNIER;JEAN\n213565488;DUPOND;MARC"
# students_serial(string_students)

def best_students(dict):
    average_dict = {}
    final_list = []
    for e in dict:
        average_dict.update({e: sum(dict[e])/len(dict[e])})
    for e2 in average_dict:
        if average_dict[e2] == average_dict[max(average_dict)]:
            final_list.append(e2)
    print(final_list)
    return final_list


dict_of_grads = {
    'Denis': [5, 2, 7],
    'Ulys': [20, 19, 20],
    'Julien': [20, 20, 19],
    'Theo': [14, 10, 17]
    }
best_students(dict_of_grads)




