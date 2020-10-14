import math


def rectangle(width, length):
    area = width * length
    perimeter = (width+length)*2
    return area, perimeter


def circle(radius):
    area = math.pi * math.sqrt(radius)
    perimeter = 2 * math.pi * radius
    return area, perimeter


def prism(width, length, height):
    base_area, base_perimeter = rectangle(width, length)
    area = 2 * base_area + base_perimeter * height
    volume = base_area * height
    return area, volume


def cylinder(radius, height):
    base_area, base_perimeter = circle(radius)
    volume = base_area * height
    return volume


def sort_list(l: list, mode="asc"):
    l_str = [str(x) for x in l]
    l_str.sort(reverse=True if mode == "desc" else False)
    l = [int(x) if x.isdigit() else x for x in l_str]
    return l


#print(sort_list(['are', '75ok', 'zer', 'zzr', 80, 1]))


def phone_initial(d: dict, initial: chr(1) = "a"):
    return [x for i, x in d.items() if i[0] == initial.lower()]


# print(phone_initial({
#     "ok": 41541,
#     "ko": 15415615,
#     "oi": 1515151,
#     "albatross": 485
# }))


def rude_repertory():
    dictionary = {
        "foo": 454808,
        "bar": 447865
    }
    choice = 'z'
    while 'q' != choice.lower():
        xpctd = False
        while not xpctd:
            choice = input("""L to list
            A to add
            S to sdelete
            Q to quit""")
            try:
                choice = choice[0]
                xpctd = True
            except ValueError:
                xpctd = False
        print(choice)
        if choice == 'l':
            print(dictionary)
        elif choice == 'a':
            new_guy = input("name pliz:")
            aphonenbr = False
            while not aphonenbr:
                try:
                    guyzfone = int(input("the number of the phone is què ??"))
                    aphonenbr = True
                except ValueError:
                    print("wtf is dis ??! dats no phone nbr")
                    aphonenbr = False
            dictionary[new_guy] = guyzfone
            print(f"is ok, {new_guy}'s phone is saved")
        elif choice == 's':
            to_delete = input("who you wanna kill ? (enter name or phone nbr)")
            if to_delete in dictionary:
                print(f"poppin {to_delete}'s record (phone was {dictionary[to_delete]})")
                dictionary.pop(to_delete)
            elif to_delete.isdigit() and int(to_delete) in list(dictionary.values()):
                key = list(dictionary.keys())[list(dictionary.values()).index(int(to_delete))]
                print(f"poppin {key}'s record (phone was {to_delete})")
                dictionary.pop(key)
            else:
                print("no exist fck off")
        elif choice =="q":
            break
        else:
            print("don't be a twat...")


rude_repertory()





