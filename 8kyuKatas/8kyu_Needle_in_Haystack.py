"""
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
Note: In COBOL, it should return "found the needle at position 6"
"""

# My Solution
def find_needle(haystack):
    # your code here
    index_needle = haystack.index('needle')
    return f"found the needle at position {index_needle}"

# Shorter version of Mine:
def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

# Or:
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
    
# Longer version:
def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i