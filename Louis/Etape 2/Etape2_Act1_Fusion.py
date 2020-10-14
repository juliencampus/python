
import itertools as it

def main():


    list_int = list(range(10))
    list_str = ["Jason", "Marty", "Kevin", "Barbara", "Gouniafé"]

    print(list_int)




    print([x for x in it.chain.from_iterable(it.zip_longest(list_int, list_str)) if x])



if __name__ == "__main__":
    main()