def rps(p1, p2):
    #your code here
    if p1 == p2:
        return 'Draw!'
    
    rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    
    if (p2 == rules[p1]):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'