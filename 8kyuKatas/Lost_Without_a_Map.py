'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

# My Solution
def maps(a):
    data = []
    for int in a:
        int *=2
        data.append(int)
    return data
    
 # Alternative Solution
 def maps(a):
    return [2 * x for x in a]
    
 # Alternate Solution
 def maps(a):
    return map(lambda x:2*x, a)
    
 # Alternate Solution
 def maps(a):
    num = []
    for i in a:
        num.append(i * 2)
    return num