"""Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined"""


# My Answer
def count_sheep(sheep):
    count = 0
    for number in sheep:
        if number == True:
            count += 1
    return count
    

# Alternate Answer
def count_sheep(sheep):
    return len([x for x in sheep if x])
    

# Alternate Solution
def count_sheep(sheep):
    return sheep.count(True)

