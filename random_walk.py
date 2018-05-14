#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     12/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import random

def random_walk1(n):
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x,y)

def testRandomWalk1():
    for i in range(25):
        walk = random_walk1(10)
        print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

def random_walk2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return(x, y)

def testRandomWalk2():
    for i in range(25):
        walk = random_walk2(10)
        print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))


def monteCarlo():
    number_of_walks = 20000

    for walk_length in range(1, 31):
        no_transport = 0 # Number of walks 4 or fewer blocks from home
        for i in range(number_of_walks):
            (x, y) = random_walk2(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 5:
                no_transport +=1
        no_transport_percentage = float(no_transport) / number_of_walks
        print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)




def main():
    #testRandomWalk1()
    #testRandomWalk2()
    monteCarlo()
    pass

if __name__ == '__main__':
    main()
