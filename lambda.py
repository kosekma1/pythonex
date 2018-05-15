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

def f(x):
    return 3*x + 1

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

def main():

    print(f(2))

    g = lambda x: 3*x +1 #lambda expression
    print(g(2))

    # Combine first name and last name into a single "Full Name"
    full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
    print(full_name("    leonhard", "EULER"))

    scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke",
    "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wels", "Leigh Brackett"]
    help(scifi_authors.sort)
    scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
    print(scifi_authors)

    fQuadra = build_quadratic_function(2, 3, -5)
    print(fQuadra(5))

    print(build_quadratic_function(3,0,1)(2)) # 3x^2+1 evaluated for x=2

    pass

if __name__ == '__main__':
    main()
