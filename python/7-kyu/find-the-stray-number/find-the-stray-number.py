def stray(arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    else:
        unequal = [n for n in arr if n != arr[0]]
        return unequal[0]