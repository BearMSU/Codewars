def count_sheep(n):
    # your code
    sheep_string = ""
    for sheep in range(1, n + 1):
        sheep_string += f"{sheep} sheep...".replace("\n", "")
    return sheep_string