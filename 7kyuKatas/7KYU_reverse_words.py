"""
Instructions:

Complete the function that accepts a string parameter, and reverses each word in the string.

All spaces in the string should be retained.

Examples:

"This is an example!" ==> "sihT si na !elpmaxe"
"doulbe spaces"       ==> "elbuod  secaps"
"""

def reverse_word(text):
	return " ".join(word[::-1] for word in text.splie(" "))
	