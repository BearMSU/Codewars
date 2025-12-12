"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

# My Solution
def descending_order(num):
    return int("".join(sorted([num for num in str(num)], reverse=True)))
    
# Alternate Solution
def descending_order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)

# Solution 3:
def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))

# Solution 4:
def Descending_Order(num):
    digits = []
    
    while num > 0:
        new_num = num // 10
        digits.append(num - new_num*10)
        num = new_num
        
    out = 0
    for i, digit in enumerate(sorted(digits)):
        out += digit * 10**i
        
    return out

# Solution 5:
def Descending_Order(num):
    #Bust a move right here
    list=[]
    while num/10 !=0 :
        list.append(num%10)
        num=num/10
    list.append(num)
    list.sort()
    print list
    numb=0;
    i=0
    print i
    while i <len(list):
        numb+=list[i]*pow(10,i)
        i+=1
        print numb
    return numb   