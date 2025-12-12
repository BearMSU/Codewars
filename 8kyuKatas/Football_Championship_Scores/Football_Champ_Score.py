# Football Scores Calculation Function
def points(games):
    total = 0
    for score in games:
        game = score.split(":")
        if game[0] > game[1]:
            total += 3
        elif game[0] == game[1]:
            total +=1
    return total
            