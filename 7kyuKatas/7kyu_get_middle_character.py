"""
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
"""

# My Solution
def get_middle(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        mri = len(s) // 2
        return s[mri - 1 : mri + 1]

# Another Solution:
def get_middle(s):
    return s[(len(s) - 1) // 2 : (len(s) + 2) // 2]