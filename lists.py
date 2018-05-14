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


def lists():
    #two ways of definition
    example = list()
    exmaple =[]

    #order in lists is important

    primes = [2,3,5,7,11,13]
    print(primes)

    primes.append(17)
    primes.append(19)
    print(primes)

    #addreses via indexes
    print(primes[0]) #first element
    print(primes[1]) #second element

    print(primes[-1]) #the last element
    print(primes[-2]) #the one element before last

    #slicing
    print(primes[2:5]) #from index 2 to 4
    print(primes[0:6])  #from index 0 to 5

    #list can cointain multiple datatypes in the same list
    example = [128, True, "Alpha", 1.732, [64, False]]
    print(example)

    rolls = [4,7,2,7,12,4,7] #list can contain duplicates
    print(rolls)

    numbers = [1,2,3]
    letters = ['a','b','c']

    #concatenation
    print(numbers + letters)
    print(letters + numbers)

    dir(numbers) #shows all methods
    help(numbers.reverse) #show help of method reverse



def main():
    lists()
    pass

if __name__ == '__main__':
    main()
