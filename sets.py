#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     09/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def setBasicMethods():
    #dir(set)
    #help(set.add)

    #in set is order not important

    example = set()
    example.add(42)
    example.add(False)
    example.add(3.14159)
    example.add("Thorium")
    print(example)

    example.add(42) #has no effect, set contains only unique elements
    print(example)

    print(len(example)) #number of elements in the set

    example.remove(42)
    print(example)
    print(len(example))
    #example.remove(50)  #raise a key error, element is not in the set

    example.discard(50) #similar to remove, but raise nothing if element is not in the set

    example2 = set([28, True, 2.71828, "Helium"])
    print(example2)
    example2.clear(); #remove all elements
    print(len(example2))

def setOperations():
    odds = set([1,3,5,7,9])
    evens = set([2,4,6,8,10])
    primes = set([2,3,5,7])
    compositest = set([4,6,8,9,10])

    #union
    print(odds.union(evens))
    print(evens.union(odds))

    #intersection
    print(odds.intersection(primes))
    print(primes.intersection(evens))
    print(evens.intersection(odds)) #no intersection
    print(primes.union(compositest))

    #is in
    print(2 in primes)
    print(6 in odds)
    print(9 not in evens)

    dir(primes) #show all methods of sets





def main():
    #setBasicMethods()
    setOperations()

if __name__ == '__main__':
    main()
