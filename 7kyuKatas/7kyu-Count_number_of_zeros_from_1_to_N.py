# Count number of zeros from 1 to N

# Solution:
def count_zeros(x):
    # your code here
    count = 0
    for i in range(1, x + 1):
        s = str(i)
        for digit in s:
            if digit == '0':
                count += 1
    return count
    
# Alternate Solution:
def count_zeros(x):
    return "".join(map(str, range(10, x + 1))).count("0")
    
# Alternate Solution 2:
def count_zeros(x):
    count=0
    for num in range(1,x+1):
        count+=str(num).count('0')
    return count

# Alternate Solution 3:
def count_zeros(x):
    return sum(str(i).count('0') for i in range(1, x + 1))