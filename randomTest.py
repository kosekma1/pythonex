#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     11/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import random

def testRandom():
    print(dir(random))
    print(help(random.random))


def displayRandomNumbers():
    for i in range(10):
        print(random.random())

    # Generate random numbers from interval [3, 7)
    print()
    for i in range(10):
        print(random.random()*4 + 3)

    # Other way - uniform function
    print()
    for i in range(10):
        print(random.uniform(3,7))

    # normal distribution
    print()
    for i in range(20):
        print(random.normalvariate(5,0.2))     #(mean, standard deviation)


    # range
    print()
    for i in range(20):
        print(random.randint(1,6))

    # kamen nuzky papir
    outcomes = ['rock', 'paper','scissors']
    print()
    for i in range(20):
        print(random.choice(outcomes))






def main():
    #testRandom()
    displayRandomNumbers()
    pass

if __name__ == '__main__':
    main()
