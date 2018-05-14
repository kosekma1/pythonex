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

import math
import time

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""

    if n==1:
        return False  # 1 is not prime

    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def time_function():
    t0 = time.time()
    for n in range(1,100000):
        is_prime_v1(n)
    t1 = time.time()
    print("Time required ", t1 - t0)

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n==1:
        return False  # 1 is not prime

    max_divisor = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_divisor):
        if n % i == 0:
            return False
    return True

def time_function2():
    t0 = time.time()
    for n in range(1,100000):
        is_prime_v2(n)
    t1 = time.time()
    print("Time required ", t1 - t0)


def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n==1:
        return False  # 1 is not prime

    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    if n % 2 > 0:
        step = 2
    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divisor, step):
        if n % i == 0:
            return False
    return True

def time_function3():
    t0 = time.time()
    for n in range(1,100000):
        is_prime_v3(n)
    t1 = time.time()
    print("Time required ", t1 - t0)


def main():

    if(is_prime_v1(990)):
        print("Is prime")
    else:
        print("Not prime")

    #time_function()
    #time_function2()
    time_function3()


if __name__ == '__main__':
    main()
