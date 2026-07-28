def square_digits(num):
    # Your code here
    num_list = list(map(int, str(num)))
    squared_arr = [n ** 2 for n in num_list]
    squared_nums = "".join(map(str, squared_arr))
    return int(squared_nums)