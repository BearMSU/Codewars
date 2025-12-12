"""Jaden Casing Strings:

Jaden Smith, the son of Will Smith, is the star of films such as 
The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word. 
For simplicity, you'll have to capitalize each word, 
check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real" """

# Solution 1:
def to_jaden_case(string):
    text = string.split(" ")
    jayden = []
    for word in text:
        jayden.append(word.capitalize())
    return(" ".join(jayden))
    
# Solution 2:
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
    
# Solution 3:
def to_jaden_case(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)
    
# Solution 4:
def to_jaden_case(string):
    words = string.split(" ")
    output = ""
    for word in words:
        corrected = word.capitalize()
        output += corrected + " "
        
    return output[0:-1]
# [0:-1] to take from begining to last one excluding the last one " "
# word.capitalize = to capitalize the first letter of an string