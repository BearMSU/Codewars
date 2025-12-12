"""
Loading Sum of two lowest positive integers

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

# My Solution:
def sum_two_smallest_numbers(numbers):
    sort = sorted(numbers)
    x = int(sort[0])
    y = int(sort[1])
    return x + y
    
# Alternate Solution:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# Solution 3:
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]

# Solution 4:
def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]