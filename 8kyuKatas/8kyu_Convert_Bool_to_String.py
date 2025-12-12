"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""

# My solution:
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'
        
# Other Solution
def bool_to_word(bool):
    return "Yes" if bool else "No"
    
# Simpler of Mine
def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'