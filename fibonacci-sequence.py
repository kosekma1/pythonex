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

def fibIter(n):

    first=1
    second=1
    sum = 0
    for i in range(2,n):
        sum = first + second;
        first = second
        second = sum

    if(sum>0):
        return sum
    else:
        return 1


from functools import lru_cache    # decorator
# LRU Cache = Least Recently Used Cache

@lru_cache(maxsize = 1000)
def fibonacci(n):

    # Check that input is a positive integer
    if(type(n) != int):
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_cache = {}

def fibonacciMemoization(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n > 2:
        value = fibonacciMemoization(n-1) + fibonacciMemoization(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value




def main():
    for n in range(1,1001):
        print(n, ": ", fibIter(n))

    for n in range(1,1001):
        print(n, ": ", fibonacciMemoization(n))


    for n in range(1,1001):
        print(n, ": ", fibonacci(n))  # Memoization via decorator


    #fibonacci(2.4)

    for n in range(1, 51):
        print(fibonacci(n+1) / fibonacci(n))

    pass



if __name__ == '__main__':
    main()
