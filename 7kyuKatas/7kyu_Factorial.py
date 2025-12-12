'''
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type 
ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or 
ValueError (Python) or return -1 (C).
'''

# My solution:
def factorial(n):
    import math
    if n < 0 or n > 12:
        raise ValueError("Number outside accepted range.")
    return math.factorial(n)
    

# Alternate Solution:
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n*factorial(n-1)

# Alternate Solution 2:
def factorial(n):
    output = 1
    if n > 12 or n < 0:
        raise ValueError
    else:
        for x in range(1, n+1):
            output *= x
        return output

# Alternate Solution 3:
def factorial(n):
    if n>12 or n<0:
        raise ValueError
    if n==0:
        return 1
    return n*factorial(n-1)