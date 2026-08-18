def merge_arrays(arr1, arr2):
    for num in arr2:
        arr1.append(num)
    unique = sorted(set(arr1))
    return list(unique)