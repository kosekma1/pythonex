#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     10/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def tuples():

    # list
    prime_numbers = [2,3,5,7,11,13,17]

    # tuple contain data surrounded by parentheses
    # tuple can not be changed, but list can

    perfect_squares = (1,4,9,16,25,36)

    print("# Squares = ", len(perfect_squares))

    for n in perfect_squares:
        print("Square: ", n)


    print("List methods")
    print(dir(prime_numbers))
    print(80*"-")
    print("Tuple methods")
    print(dir(perfect_squares))

    # lists occupy more memoery than tuples
    import sys
    print("sys methods")
    print(dir(sys))

    print(help(sys.getsizeof))

    list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
    tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

    print("Different size of tuples and lists")
    print("List size = ", sys.getsizeof(list_eg))
    print("Tuple size = ", sys.getsizeof(tuple_eg))

    # Lists
    # - add data
    # - remove data
    # - change data

    # Tuples
    # Cannot be changed
    # "Immutable"
    # Made more quickly

    # test quickly
    import timeit

    list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
    tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

    print("Time to create tuples and lists")
    print("List time: ", list_test)
    print("Tuple time: ", tuple_test)

    pass

def essentialsTuples():
    empty_tuple = ()
    test1 = ("a",) # must be comma at the end, if not than it is string
    test2 = ("a", "b")
    test3 = ("a", "b","c")

    print(empty_tuple)
    print(test1)
    print(test2)
    print(test3)

    # Alternative Construction of Tuples
    test1 = 1,
    test2 = 1,2
    test3 = 1,2,3
    print(test1)
    print(test2)
    print(test3)
    print(type(test1))
    print(type(test2))
    print(type(test3))

    # example 1
    # (age, country, knows_python)
    survey = (27, "Vietnam", True)

    age = survey[0]
    country = survey[1]
    knows_python = survey[2]

    print("Example 1")
    print("Age =", age)
    print("Country =", country)
    print("Knows Python?", knows_python)

    # example 2
    survey2 = (21, "Switzerland", False)
    age, country, knows_python = survey2  # assignes automatically elements to variables
    print("Example 2")
    print("Age =", age)
    print("Country =", country)
    print("Knows Python?", knows_python)

    country = ("Australia") # assignes String to country
    print(country)
    print(type(country))

    country = ("Australia",) # assignes String to country, see comma at the end
    print(country)
    print(type(country))

    # error - number of variables must match number of values in tuple
    try:
        a, b, c = (1, 2, 3, 4)
        x, y, z = (1, 2)
    except ValueError:
        print("Number of variables and values in tuple does not match")


def main():
    #tuples()
    essentialsTuples()
    pass

if __name__ == '__main__':
    main()

