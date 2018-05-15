#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     15/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

def testMapArea():
    radii = [2, 5, 7.1, 0.3, 10]

    # Compute ares for many 'r'

    # Method 1: Direct method
    areas = []
    for r in radii:
        a = area(r)
        areas.append(a)

    print(areas)

    # Method 2: Use 'map' function
    result = map(area, radii)  # map(function, data to iterate over) ... returns iterator over f(a1), f(a2), ... , f(n)
    print(list(result))

def convertCelsiusToFarenheit(t):
    city = t[0]
    temperature = t[1]*float(9/5)+32
    return (city, temperature)

def testMapConvertTemperature():
    """Convert list of celsiues to Farenheit"""
    temps =[("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27) ,
    ("New York", 28), ("London", 22), ("Beijing", 32)]

    c_to_f = lambda data: (data[0], (9/5)*data[1]+32) # Function on one line

    #result = map(convertCelsiusToFarenheit, temps)
    result = map(c_to_f, temps)
    print(list(result))

def testFilter():
    import statistics

    data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
    print(data)
    avg = statistics.mean(data) # computes average of the data
    print("Average = ", avg)

    # filter values that are above average
    result = filter(lambda x: x > avg, data)
    print("Above average values: ", list(result))

    result = filter(lambda x: x < avg, data)
    print("Below average values: ", list(result))

def testRemoveMissingDataFilter():
    # Remove missing data
    countries = ["","Argentina", "Brazil", "Chile", "","Colombia", "", "Ecuador","","","Venezuela"]
    print(list(filter(None, countries)))


def testReduceFunction():
    from functools import reduce

    # Multiply all numbers in a list be reduce
    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    multiplier = lambda x, y: x*y

    print(reduce(multiplier, data))

    # Multiply all numbers in a list be reduce
    product = 1
    for x in data:
        product = product * x

    print(product)

def main():
    #testMapArea()
    #testMapConvertTemperature()
    #testFilter()
    #testRemoveMissingDataFilter()
    testReduceFunction()
    pass

if __name__ == '__main__':
    main()
