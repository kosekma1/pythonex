#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     16/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def sortingTest1():

    # list of elements
    earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

    earth_metals.sort() # sort alphabetically
    print(earth_metals)

    earth_metals.sort(reverse = True) # sort alphabetically in reverse order
    print(earth_metals)

    # tuple of elements
    earth_metals = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
    earth_metals.sort() # error - tuple can not be sorted by sort() = can not be changed = immutable

def sortingTest2():

    help(list.sort)

    planets = [
        # name, radius, density, distance from Sun
        ("Mercury", 2440, 5.43, 0.395),
        ("Venus", 6052, 5.24, 0.723),
        ("Earth", 6378, 5.52, 1.000),
        ("Mars", 3396, 3.93, 1.530),
        ("Jupiter", 71492, 1.33, 5.210),
        ("Saturn", 60268, 0.69, 9.551),
        ("Uranus", 25559, 1.27, 19.213),
        ("Neptune", 24764, 1.46, 30.070),
        ]
    size = lambda planet: planet[1]  # sort by radius
    planets.sort(key=size, reverse = True)
    print(planets)

    density = lambda planet: planet[2]   # sort by density
    planets.sort(key=density)
    print(planets)


def sortingTest3():
    help(sorted)
    earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
    sorted_earth_metals = sorted(earth_metals) # return new sorted list
    print(sorted_earth_metals)
    print(earth_metals)

    data = (7,2,5,6,1,3,9,10,4,8) # tuple
    sorted_data = sorted(data) # sorted can sort tuple and return sorted list
    print(sorted_data)

    sorted_string = sorted("Alphabetical")
    print(sorted_string)

def main():
    #sortingTest1()
    #sortingTest2()
    sortingTest3()


    pass

if __name__ == '__main__':
    main()
