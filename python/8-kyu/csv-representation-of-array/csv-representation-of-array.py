def to_csv_text(array):
    # good luck
    return '\n'.join(','.join(map(str, n)) for n in array)