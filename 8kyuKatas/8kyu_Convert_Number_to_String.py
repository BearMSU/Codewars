"""
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
"""

# My Solution:
def number_to_string(num):
    return str(num)
    
# Crazy Solution:
def number_to_string(num):
    i = 0
    flag = False
    if num >= 0:
        flag = True
    num = abs(num)
    num_str = ''
    for i in range(len(str(num))):
        n = num % 10
        if n == 0:
            num_str += '0'
        elif n == 1:
            num_str += '1'
        elif n == 2:
            num_str += '2'
        elif n == 3:
            num_str += '3'
        elif n == 4:
            num_str += '4'
        elif n == 5:
            num_str += '5'
        elif n == 6:
            num_str += '6'
        elif n == 7:
            num_str += '7'
        elif n == 8:
            num_str += '8'
        elif n == 9:
            num_str += '9'
        num = num // 10
    return num_str[::-1] if flag else '-'+num_str[::-1]