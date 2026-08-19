def count_sheep(n):
    # your code
    string = ""
    for sheep in range(1, n + 1):
        string += f"{sheep} sheep...".replace("\n", "")
    return string