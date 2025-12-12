""" Binary Addition
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary) """

# My Solution:
def add_binary(a,b):
    c = a + b
    return(bin(c)[2:])

# My Solution 2:
def add_binary(a,b):
    return(bin(a + b)[2:])

# Another Solution:
def add_binary(a,b):
    return '{0:b}'.format(a + b)
    
# Another Solution 2:
def add_binary(a, b):
    return format(a + b, 'b')

# Another Solution 3:
def add_binary(a,b):
    return f"{a + b:b}"