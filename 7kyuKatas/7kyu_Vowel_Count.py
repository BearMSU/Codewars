"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

# My Solution:
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            count += 1
    return count

# Another Solution:
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# One More:
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])