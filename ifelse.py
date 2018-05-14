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


def enterText():
    inputText = input("Please enter a test string: ")
    if len(inputText) < 6:
        print("Your string is too short.")
        print("Please enter a string with at least 6 characters")


def enterNumber():
    inputNumber = input("Please neter an integer: ")
    number = int(inputNumber)

    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd")

def enterTriangle():
    a = int(input("The length of side a= "))
    b = int(input("The length of side b= "))
    c = int(input("The length of side c= "))


    if a+b>c and a+c>b and b+c>a and a!=0 and b!=0 and c!=0:
        if a!=b and b!=c and a!=c:
            print("This is a scalene triangle.")
        elif a==b and b==c:
            print("This is an equilateral triangle.")
        else:
            print("This is an isosceles triangle.")
    else:
        print("Triangle does not exist.")


def main():
    #enterText()
    #enterNumber()
    enterTriangle()

if __name__ == '__main__':
    main()
