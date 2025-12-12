# Ok Answer, but not really best practices and could fail potentially
def points(games):
    points = 0
    for game in games:
        x = int(game[0])
        y = int(game[2])
        if x>y:
            points += 3
        elif x==y:
            points += 1
    return points


# Better solution, but not as simplistic as others
def points(games): 
    total = 0
    a = len(games) 
    for i in range(0,a): 
            a = games[i].split(':') 
            if a[0] > a[1]: 
                total = total + 3 
            if a[0] == a[1]: 
                total = total + 1 
            if a[0] < a[1]: 
                total = total + 0 
    return total