def each_cons(lst, n):
    # your solution here
    return[lst[i: i+n] for i in range(len(lst) - n + 1)]