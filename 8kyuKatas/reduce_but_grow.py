"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

# My Solution (weak but works):
def grow(arr):
    total = 1
    for x in arr:
        total *= x
    return total
    
# Better solution:
import math
def grow(arr):
    return math.prod(arr)


