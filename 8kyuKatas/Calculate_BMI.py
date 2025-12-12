"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""


# My Solution:
def bmi(weight, height):
    #your code here
    bmi = weight / height**2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"
        
# Other Solution:
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
    

# Weird Solution:
def bmi(weight, height):
    ratio = weight / height ** 2
    
    if ratio > 18.5:
        if ratio > 25:
            if ratio > 30:
                return 'Obese'
            return 'Overweight'
        return 'Normal'
    return 'Underweight'

# Solution 2:
bmi=lambda w,h:next(s for s,t in zip("Obese Overweight Normal Underweight".split(),(30,25,18.5,0))if w/h/h>t)

# Solution 3:
def bmi(weight, height):
    index = weight/height/height
    return "Underweight" if index <= 18.5 else "Normal" if index <= 25.0 else\
      "Overweight" if index <= 30.0 else "Obese"
      
# Solution 4:
def bmi(weight, height):
    result = weight / height / height
    return "Underweight Normal Overweight Obese".split()[
            (result > 18.5) +
            (result > 25.0) +
            (result > 30.0)]