#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     13/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# List Comprehensions
#
# [expr for val in collection]
# [expr for val in collection if <test>]
# [expr for val in collection if <test> and <test2>]
# [expr for val1 in collection1 and val2 in collection2]

def listExample1():
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    print(squares)


def listExample2():
    squares = [i**2 for i in range(10,101)]
    print(squares)

def listExample3():
    #reminders5 = [x**2 % 5 for x in range(1,101)]
    #print(reminders5)

    reminders11 = [x**2 % 11 for x in range(1,101)]
    print(reminders11)


def listExample4():
    import csv

    path = "C:\Programy\PythonProjects\movies.csv"
    file = open(path, newline='')

    reader = csv.reader(file)
    header = next(reader)

    movies = []
    for row in reader:
        movies.append(row[1])

    print("Movies loaded from CSV")

    #gmovies = []
    #for title in movies:
    #    if title.startswith("G"):
    #        gmovies.append(title)
    #print(gmovies)

    gmovies = [title for title in movies if title.startswith("G")]
    print(gmovies)


def listExample5():
    """Finding movie with year release below 2000"""

    import csv
    import random
    path = "C:\Programy\PythonProjects\movies.csv"
    file = open(path, newline='')

    reader = csv.reader(file)
    header = next(reader)

    movies = []
    for row in reader:
        t = row[1].split('(')
        #t[1] = int(t[1].replace(')',''))
        t[1] = int(random.uniform(1990,2018))     # random generating years of release
        t[0] = t[0].strip()
        movies.append((t[0],t[1])) # save to list as tuples
        print(t)

    print("Movies loaded from CSV")

    #Find movies with release before 2000
    pre2k = [title for (title, year) in movies if year < 2000]
    print(pre2k)


def listExample6():
    reminders15 = [x**2 % 15 for x in range(1,101) if x<10]
    print(reminders15)


def listExample7():
    """Scalar multiplication"""
    v = [2, -3, 1] # vector
    result = [i*4 for i in v] # scalar multiplication
    print(result)

def listExample8():
    """Cartesian Product"""
    A = [1,3,5,7]
    B = [2,4,6,8]

    cartesian_product = [(a,b) for a in A for b in B]
    print(cartesian_product)


def main():
    #listExample1()
    #listExample2()
    #listExample3()
    #listExample4()
    #listExample5()
    #listExample6()
    #listExample7()
    #listExample8()
    pass

if __name__ == '__main__':
    main()
