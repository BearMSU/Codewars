def fake_bin(x):
    fake_string = ""
    for n in x:
        if int(n) < 5:
            fake_string += '0'
        else:
            fake_string += '1'
    return fake_string