def open_or_senior(data):
    membership = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            membership.append('Senior')
        else:
            membership.append('Open')
    return membership